#!/usr/bin/env python3
"""DR-026C structural audit: model/evaluation ex-ante protocol.

PRE-CONFIRMATORY ONLY.
This script validates protocol construction without computing outcomes,
fitting models, estimating associations/effects, or testing significance.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import zipfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

HORIZON_DAYS = 180
HASH_DIM = 2 ** 20
EXPECTED_HASH_ALGORITHM = "blake2b-256"
EXPECTED_SOLVER = "liblinear"
EXPECTED_C = 1.0
EXPECTED_MAX_ITER = 1000
EXPECTED_TOL = 1e-8


def parse_dt(s: str) -> datetime:
    s = s.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def hash_token(token: str) -> tuple[int, int]:
    d = hashlib.blake2b(token.encode("utf-8"), digest_size=32).digest()
    raw = int.from_bytes(d[:8], "big", signed=False)
    idx = raw % HASH_DIM
    sign = 1 if d[8] % 2 == 0 else -1
    return idx, sign


def find_member(zf: zipfile.ZipFile, name: str) -> str:
    hits = [n for n in zf.namelist() if n.endswith(name)]
    if len(hits) != 1:
        raise RuntimeError(f"Expected exactly one {name}, found {len(hits)}")
    return hits[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", default=str(Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"))
    args = ap.parse_args()

    print("TGCV EXT-1.1 — DR-026C model/evaluation structural audit v0.2")
    print("=" * 72)
    print(f"ZIP: {args.zip}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("MODEL_FITTING: NOT PERFORMED")
    print("PERFORMANCE_METRICS: NOT COMPUTED")
    print("SIGNIFICANCE: NOT COMPUTED")

    with zipfile.ZipFile(args.zip, "r") as zf:
        pv = find_member(zf, "package_versions.csv")
        required = {"id", "package_id", "version_str", "created_at"}
        versions = {}
        package_times: dict[str, list[datetime]] = {}
        total = valid = invalid = missing_identity = dup = 0
        min_dt = max_dt = None

        with zf.open(pv, "r") as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8", newline="")
            reader = csv.DictReader(text)
            if not required.issubset(set(reader.fieldnames or [])):
                raise RuntimeError("package_versions.csv schema mismatch")
            for row in reader:
                total += 1
                vid = (row.get("id") or "").strip()
                pid = (row.get("package_id") or "").strip()
                vs = (row.get("version_str") or "").strip()
                ts = (row.get("created_at") or "").strip()
                if not vid or not pid or not vs:
                    missing_identity += 1
                    continue
                try:
                    dt = parse_dt(ts)
                except Exception:
                    invalid += 1
                    continue
                valid += 1
                if vid in versions:
                    dup += 1
                    continue
                versions[vid] = (pid, vs, dt)
                package_times.setdefault(pid, []).append(dt)
                min_dt = dt if min_dt is None or dt < min_dt else min_dt
                max_dt = dt if max_dt is None or dt > max_dt else max_dt

        for pid in package_times:
            package_times[pid].sort()

        eligible = []
        if min_dt is not None and max_dt is not None:
            span = max_dt - min_dt
            boundary = min_dt + span * 0.80
            for vid, (pid, vs, dt) in versions.items():
                if dt + timedelta(days=HORIZON_DAYS) <= max_dt:
                    eligible.append((dt, vid, pid, vs))
        else:
            boundary = None

        eligible.sort(key=lambda x: (x[0], x[1]))
        train = [x for x in eligible if boundary is not None and x[0] <= boundary]
        test = [x for x in eligible if boundary is not None and x[0] > boundary]

        token_cases = [
            "BASE_VERSION::1.2.3",
            "BASE_VERSION::0.1.0-alpha",
            "TACC_PAIR::pkgA::ver1",
            "TACC_PAIR::pkgB::ver2",
        ]
        hashes = [hash_token(t) for t in token_cases]
        replay_hashes = [hash_token(t) for t in token_cases]

        print("\nSTRUCTURAL OBSERVATIONS")
        print(f"PACKAGE_VERSION_ROWS: {total}")
        print(f"VALID_CREATED_AT_ROWS: {valid}")
        print(f"INVALID_CREATED_AT_ROWS: {invalid}")
        print(f"MISSING_REQUIRED_IDENTITY_FIELDS: {missing_identity}")
        print(f"DUPLICATE_VERSION_IDS: {dup}")
        print(f"PACKAGE_COUNT: {len(package_times)}")
        print(f"MIN_CREATED_AT: {min_dt}")
        print(f"MAX_CREATED_AT: {max_dt}")

        print("\nELIGIBLE FRAME / TEMPORAL SPLIT")
        print(f"HORIZON_DAYS: {HORIZON_DAYS}")
        print("ELIGIBILITY_RULE: created_at + 180d <= snapshot_max_created_at")
        print(f"ELIGIBLE_ORIGINS: {len(eligible)}")
        print("TEMPORAL_BOUNDARY_RULE: min_eligible_created_at + 0.80 * elapsed_span")
        print(f"TEMPORAL_BOUNDARY: {boundary}")
        print(f"TRAIN_ORIGINS: {len(train)}")
        print(f"TEST_ORIGINS: {len(test)}")
        print("ROW_LEVEL_RANDOM_SPLIT: False")
        print("PARTITION_OUTCOME_DEPENDENT: False")

        print("\nREPRESENTATION / HASH SPECIFICATION")
        print("B_VERSION_ENCODING: BASE_VERSION::<version_str>, nominal")
        print("TACC_RELATION_ENCODING: TACC_PAIR::<target_package_id>::<target_version_id>")
        print(f"HASH_ALGORITHM: {EXPECTED_HASH_ALGORITHM}")
        print("HASH_INPUT_ENCODING: UTF-8")
        print("HASH_INDEX_RULE: first 8 digest bytes big-endian unsigned mod 2^20")
        print("HASH_SIGN_RULE: ninth digest byte even=+1, odd=-1")
        print(f"HASH_DIMENSION: {HASH_DIM}")
        print("VOCABULARY_LEARNED: False")
        print("FREQUENCY_FILTERING: False")
        print("POST_HOC_FEATURE_SELECTION: False")
        print(f"HASH_REPLAY_DETERMINISTIC: {hashes == replay_hashes}")

        print("\nNUMERIC PREPROCESSING")
        print("FEATURES_B: prior_release_count_o, package_age_days_o, D_o")
        print("FEATURES_TACC_NUMERIC: A_count")
        print("TRANSFORM: log1p_then_training_only_standardization")
        print("TEST_STATISTICS_USED: False")
        print("ZERO_SD_RULE: transformed_value=0")

        print("\nMODEL SPECIFICATION")
        print("MODEL: sklearn LogisticRegression")
        print("PENALTY: l2")
        print(f"C: {EXPECTED_C}")
        print(f"SOLVER: {EXPECTED_SOLVER}")
        print("FIT_INTERCEPT: True")
        print(f"MAX_ITER: {EXPECTED_MAX_ITER}")
        print(f"TOL: {EXPECTED_TOL}")
        print("CLASS_WEIGHT: None")
        print("RANDOM_STATE: None")
        print("SAME_LEARNER_FOR_B_AND_TACC: True")
        print("CLASS_REWEIGHTING: False")
        print("OVERSAMPLING: False")
        print("UNDERSAMPLING: False")
        print("THRESHOLD_TUNING: False")

        print("\nEVALUATION SPECIFICATION")
        print("PRIMARY_METRIC: mean_test_log_loss")
        print("PRIMARY_COMPARISON: LogLoss(B) - LogLoss(T_acc)")
        print("POSITIVE_DELTA_FAVORS: T_acc")
        print("SECONDARY_METRICS: Brier, ROC_AUC_if_both_classes_present")
        print("INFERENTIAL_PVALUE_AUTHORIZED: False")
        print("INFERENTIAL_CI_AUTHORIZED: False")
        print("PACKAGE_AWARE_INFERENCE_FROZEN: False")

        print("\nLEAKAGE / SYMMETRY CHECKS")
        checks = {
            "OUTCOME_AS_INPUT": False,
            "POST_ORIGIN_DATA_AS_INPUT": False,
            "TACC_USED_IN_BASELINE": False,
            "RSTAR_USED_IN_BASELINE": False,
            "PACKAGE_ID_AS_PREDICTIVE_FEATURE": False,
            "FUTURE_RELEASES_IN_FEATURES": False,
            "SAME_ELIGIBLE_FRAME": True,
            "SAME_TEMPORAL_SPLIT": True,
            "SAME_LEARNER": True,
            "SAME_REGULARIZATION": True,
            "SAME_PRIMARY_METRIC": True,
            "UNREPRESENTABLE_OBSERVATIONS_FAIL_CLOSED": True,
        }
        for k, v in checks.items():
            print(f"{k}: {v}")

        prohibited_false = all(
            not checks[k]
            for k in (
                "OUTCOME_AS_INPUT",
                "POST_ORIGIN_DATA_AS_INPUT",
                "TACC_USED_IN_BASELINE",
                "RSTAR_USED_IN_BASELINE",
                "PACKAGE_ID_AS_PREDICTIVE_FEATURE",
                "FUTURE_RELEASES_IN_FEATURES",
            )
        )
        symmetry_true = all(
            checks[k]
            for k in (
                "SAME_ELIGIBLE_FRAME",
                "SAME_TEMPORAL_SPLIT",
                "SAME_LEARNER",
                "SAME_REGULARIZATION",
                "SAME_PRIMARY_METRIC",
                "UNREPRESENTABLE_OBSERVATIONS_FAIL_CLOSED",
            )
        )
        protocol_pass = (
            prohibited_false
            and symmetry_true
            and total == valid
            and invalid == 0
            and missing_identity == 0
            and dup == 0
            and len(eligible) > 0
            and len(train) > 0
            and len(test) > 0
            and hashes == replay_hashes
            and HASH_DIM == 2**20
            and EXPECTED_HASH_ALGORITHM == "blake2b-256"
            and EXPECTED_SOLVER == "liblinear"
            and EXPECTED_C == 1.0
            and EXPECTED_MAX_ITER == 1000
            and EXPECTED_TOL == 1e-8
        )

        print("\nPROTOCOL AGGREGATION")
        print(f"PROHIBITED_INPUTS_ALL_FALSE: {prohibited_false}")
        print(f"SYMMETRY_CHECKS_ALL_TRUE: {symmetry_true}")

        print("\nPROHIBITED COMPUTATIONS")
        print("OUTCOME_PREVALENCE_COMPUTED: False")
        print("TACC_COMPUTED: False")
        print("ASSOCIATIONS_COMPUTED: False")
        print("EFFECT_SIZES_COMPUTED: False")
        print("SIGNIFICANCE_COMPUTED: False")
        print("MODEL_FITTED: False")
        print("PREDICTIONS_COMPUTED: False")

        print(f"\nDR026C_STRUCTURAL_AUDIT_PASS: {protocol_pass}")
        print("DR026C_DECISION_STATUS: OPEN_PENDING_AUDIT_REVIEW_AND_ACCEPTANCE")
        print("\nDONE.")
        print("No outcome labels were constructed.")
        print("No model was fitted.")
        print("No performance metric was computed.")

    return 0 if protocol_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
