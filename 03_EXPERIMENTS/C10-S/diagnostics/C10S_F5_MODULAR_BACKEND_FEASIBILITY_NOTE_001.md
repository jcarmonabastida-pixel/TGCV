# C10-S — F5 modular-resultant backend feasibility note 001

**Status:** STATIC ENGINEERING DIAGNOSTIC — NOT A SELECTED BACKEND / NOT SCIENTIFIC EXECUTION  
**Date:** 2026-11-20  
**Branch:** `research/c10s-f1-integrated-correction-20261119`  
**Scope:** exact elimination feasibility for beta-binomial score equations, M30/R20  
**Authorization:** design and static deterministic diagnostics only

## 1. Purpose

Continue the D1 backend comparison without using B2/B3 outcomes for method selection, changing frozen F1/F5 v1.0, or running stochastic data. This note records the computational implications of the already-implemented sparse exact score numerators and identifies the next viable engineering path.

## 2. Recovered and verified input layer

The current harness primitive `c10s_f5_rational_score_polynomials.py` constructs exact sparse integer numerator polynomials for the two rational score equations. Its four deterministic tests cover exact score identity, histogram validation, zero-multiplicity invariance and an M30/R20 fixture.

For the 30-world, 20-trial fixture with all 21 count cells populated:
- (\deg_\mu N_\mu=39), (\deg_\kappa N_\mu=40), 629 nonzero terms;
- (\deg_\mu N_\kappa=40), (\deg_\kappa N_\kappa=58), 1,368 nonzero terms.

This is exact algebraic construction, not root enumeration or global-MLE certification.

## 3. Modular backend checks

The available Python environment is 3.13.5 with SymPy 1.14.0. No `python-flint`, SageMath, PARI/GP binding or GMPY2 backend is installed. The governed CPython 3.12 parity check remains outstanding.

A direct SymPy resultant over the polynomial coefficient ring (GF(p)[\kappa]) was attempted on the M30/R20 score numerators and exceeded the 60-second tool ceiling. This confirms that a generic polynomial-PRS call is not an adequate implementation route in this environment; it does not falsify a purpose-built modular algorithm.

A useful tighter degree bound was derived for the resultant as a polynomial in (\kappa). Build the 79×79 Sylvester matrix from the μ-coefficients of the two score numerators. Each nonzero matrix entry is a polynomial in (\kappa). The degree of every determinant product is bounded by the maximum-weight perfect matching of this sparse Sylvester pattern, where each edge weight is the degree in (\kappa) of its corresponding entry. For the fixture, the maximum-weight assignment gives an upper bound of **3,501** on the resultant degree. The coarse dense bound would be 3,862.

This is a valid determinant-term upper bound for this fixed coefficient pattern, not an observed resultant degree. It remains far above the degree 235 observed in the earlier separate sizing fixture. Consequently, naive evaluation/interpolation at every degree up to the bound would require up to 3,502 evaluation points per good prime before CRT reconstruction, and multiple primes would multiply that cost. This is not yet a practical modular-CRT implementation.

## 4. Backend decision

Do not select generic SymPy PRS, and do not claim modular CRT is feasible merely because the coefficient field is finite. The next implementation candidate must exploit more structure than generic dense PRS or full-degree black-box interpolation.

Priority order:
1. derive a subresultant/degree-drop bound from the actual sparse coefficient support and exploit modular subresultant structure without expanding dense intermediate polynomials;
2. investigate a modular evaluation/interpolation scheme only if a tighter *proved* degree bound and rigorous coefficient reconstruction bound reduce the number of evaluations/primes to a bounded workload;
3. assess a pinned exact CAD/real-algebraic backend only in a governed environment where its availability, license, version and deterministic resource limits can be established.

An interval profile route remains a separate candidate, but it must certify all stationary points, including even-multiplicity roots, and not merely trace sign changes or follow a local conditional optimizer. Any box that cannot be excluded or uniquely certified must end in an explicit abstention.

## 5. D1 and D2 consequences

- D1 remains OPEN: no global stationary-point enumeration or outward-rounded likelihood ordering has been certified.
- D2 remains PARTIAL: sparse exact score numerator construction exists and is tested; elimination, root isolation, boundary comparison and global adjudication are not implemented.
- The F1 degree-three Sturm isolator cannot be reused unchanged for F5.
- No scientific bank, replay, bootstrap, coverage evaluation, calibration, new random seed or prospective execution was run or authorized.
- Frozen F1/F5 v1.0, C5/C0 semantics, historical B2/B3, `main`, RMA and Evidence→Claim Matrix are unchanged.

## 6. Next operation

Develop a sparse modular subresultant prototype on small exact fixtures first, cross-check every modular result against exact rational resultants at low degree, then scale the *same implementation* to the M30/R20 score numerators under a declared time/memory ceiling. In parallel, derive an interval-profile certificate specification with explicit treatment of degenerate roots. Compare only after both candidates have equivalent completeness and abstention contracts.
