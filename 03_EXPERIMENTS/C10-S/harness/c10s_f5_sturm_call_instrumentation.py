"""Per-call instrumentation for exact F5 Sturm root isolation.

Observational only: wrappers return the exact objects/results produced by the
original rational-arithmetic implementation. No tolerances or limits change.
"""
from __future__ import annotations

from fractions import Fraction
from time import perf_counter


def _coefficient_sizes(values):
    numerators = []
    denominators = []
    for value in values:
        item = Fraction(value)
        numerators.append(abs(item.numerator).bit_length())
        denominators.append(item.denominator.bit_length())
    return {
        "coefficient_count": len(numerators),
        "max_numerator_bits": max(numerators, default=0),
        "max_denominator_bits": max(denominators, default=0),
        "total_numerator_bits": sum(numerators),
        "total_denominator_bits": sum(denominators),
    }


def _integer_coefficient_sizes(sequence):
    values = [value for polynomial in sequence for value in polynomial]
    sizes = [abs(int(value)).bit_length() for value in values]
    return {
        "integer_coefficient_count": len(values),
        "max_integer_coefficient_bits": max(sizes, default=0),
        "total_integer_coefficient_bits": sum(sizes),
    }


def install_sturm_call_instrumentation(profile_module, rational_module, *, variation_evaluator=None):
    """Patch one profile module and its rational helpers; return records/restore."""
    records = []
    active = {"record": None}
    originals = {
        "isolate": profile_module._uni_isolate_squarefree_unit_roots,
        "sturm": rational_module._uni_sturm_sequence,
        "integer": rational_module._uni_sturm_integer_sequence,
        "variations": rational_module._uni_sign_variations_integer,
    }

    def timed_sturm(poly):
        started = perf_counter()
        sequence = originals["sturm"](poly)
        record = active["record"]
        if record is not None:
            flat = [value for item in sequence for value in item]
            record["sturm_sequences"].append({
                "input_degree": len(poly) - 1,
                "sequence_length": len(sequence),
                "sequence_degrees": [len(item) - 1 for item in sequence],
                "sequence_seconds": round(perf_counter() - started, 6),
                **_coefficient_sizes(flat),
            })
        return sequence

    def timed_integer(sequence):
        started = perf_counter()
        result = originals["integer"](sequence)
        record = active["record"]
        if record is not None:
            record["integer_scalings"].append({
                "seconds": round(perf_counter() - started, 6),
                **_integer_coefficient_sizes(result),
            })
        return result

    def timed_variations(sequence, point):
        started = perf_counter()
        record = active["record"]
        if variation_evaluator is None:
            result = originals["variations"](sequence, point)
        else:
            stats = record.setdefault("variation_stats", {}) if record is not None else {}
            result = variation_evaluator(sequence, point, stats=stats)
        if record is not None:
            record["variation_calls"] += 1
            record["variation_seconds"] += perf_counter() - started
        return result

    def timed_isolate(poly, **kwargs):
        record = {
            "call_index": len(records) + 1,
            "input_degree": len(poly) - 1,
            "input_coefficient_sizes": _coefficient_sizes(poly),
            "sturm_sequences": [],
            "integer_scalings": [],
            "variation_calls": 0,
            "variation_seconds": 0.0,
            "variation_stats": {},
        }
        records.append(record)
        previous = active["record"]
        active["record"] = record
        started = perf_counter()
        try:
            result = originals["isolate"](poly, **kwargs)
        finally:
            elapsed = perf_counter() - started
            active["record"] = previous
        record.update({
            "elapsed_seconds": round(elapsed, 6),
            "status": result.get("status"),
            "processed_intervals": result.get("processed_intervals", 0),
            "exact_roots": len(result.get("exact_roots", ())),
            "isolating_intervals": len(result.get("isolating_intervals", ())),
            "unresolved_intervals": len(result.get("unresolved_intervals", ())),
            "variation_calls": record["variation_calls"],
            "variation_seconds": round(record["variation_seconds"], 6),
        })
        record["integer_scalings"] = record["integer_scalings"]
        measured = (
            sum(item["sequence_seconds"] for item in record["sturm_sequences"])
            + sum(item["seconds"] for item in record["integer_scalings"])
            + record["variation_seconds"]
        )
        record["other_isolation_seconds"] = round(max(0.0, elapsed - measured), 6)
        return result

    profile_module._uni_isolate_squarefree_unit_roots = timed_isolate
    rational_module._uni_sturm_sequence = timed_sturm
    rational_module._uni_sturm_integer_sequence = timed_integer
    rational_module._uni_sign_variations_integer = timed_variations

    def restore():
        profile_module._uni_isolate_squarefree_unit_roots = originals["isolate"]
        rational_module._uni_sturm_sequence = originals["sturm"]
        rational_module._uni_sturm_integer_sequence = originals["integer"]
        rational_module._uni_sign_variations_integer = originals["variations"]

    return records, restore


def sign_variations_integer_certified_fixedpoint(sequence, point, *, stats=None):
    """Exact signs via certified fixed-point intervals, exact fallback if ambiguous.

    This is a development prototype. It uses no floating point: each Horner
    step encloses the exact value in integer units of 2**precision. A sign is
    accepted only when the interval excludes zero. Non-dyadic/out-of-domain
    points and ambiguous polynomial signs use the existing exact homogeneous
    integer-Horner calculation.
    """
    x = Fraction(point)
    if x < 0 or x > 1:
        return _exact_sign_variations(sequence, x)
    numerator, denominator = x.numerator, x.denominator
    if denominator & (denominator - 1):
        return _exact_sign_variations(sequence, x)

    signs = []
    certified = {128: 0, 256: 0}
    exact_fallback = 0
    for polynomial in sequence:
        if not polynomial:
            continue
        sign = None
        for precision in (128, 256):
            scale = 1 << precision
            lower = int(polynomial[-1]) * scale
            upper = lower
            for coefficient in reversed(polynomial[:-1]):
                lower = (lower * numerator) // denominator + int(coefficient) * scale
                product_upper = upper * numerator
                upper = -((-product_upper) // denominator) + int(coefficient) * scale
            if lower > 0:
                sign = 1
                certified[precision] += 1
                break
            if upper < 0:
                sign = -1
                certified[precision] += 1
                break
        if sign is None:
            exact_fallback += 1
            sign = _exact_integer_polynomial_sign(
                polynomial, numerator, denominator,
            )
        if sign:
            signs.append(sign)

    if stats is not None:
        stats["certified_128"] = stats.get("certified_128", 0) + certified[128]
        stats["certified_256"] = stats.get("certified_256", 0) + certified[256]
        stats["exact_fallback_polynomials"] = (
            stats.get("exact_fallback_polynomials", 0) + exact_fallback
        )
        stats["evaluated_polynomials"] = (
            stats.get("evaluated_polynomials", 0) + len(sequence)
        )
    return sum(left != right for left, right in zip(signs, signs[1:]))


def _exact_integer_polynomial_sign(polynomial, numerator, denominator):
    value = int(polynomial[-1])
    denominator_power = denominator
    for coefficient in reversed(polynomial[:-1]):
        value = value * numerator + int(coefficient) * denominator_power
        denominator_power *= denominator
    return 1 if value > 0 else (-1 if value < 0 else 0)


def _exact_sign_variations(sequence, point):
    x = Fraction(point)
    return _exact_sign_variations_numerator_denominator(
        sequence, x.numerator, x.denominator,
    )


def _exact_sign_variations_numerator_denominator(sequence, numerator, denominator):
    signs = []
    for polynomial in sequence:
        if not polynomial:
            continue
        sign = _exact_integer_polynomial_sign(
            polynomial, numerator, denominator,
        )
        if sign:
            signs.append(sign)
    return sum(left != right for left, right in zip(signs, signs[1:]))
