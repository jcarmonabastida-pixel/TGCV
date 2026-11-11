#!/usr/bin/env python3
"""Reproducible P178 focal benchmark for TGCV C10-S.

Implements the homogeneous two-signature Markov DGP in workplan §§35, 38-40.
Simulation samples each UE's exact marginal distribution of Q_B1, obtained
by dynamic programming over the two-state Markov chain. This is distributionally
identical to generating every slot trajectory, while avoiding large trajectory
arrays. It does not implement or evaluate the TGCV Analyzer.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, math, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.stats import t as student_t

LAMBDA0, LAMBDA1 = 0.25, 0.75
B01 = B10 = math.log(0.2 / 0.8)
PI_VALUES = (0.20, 0.50, 0.80)
K_VALUES = (2, 10, 50)
SCENARIOS = {"null": (0.0, 0.0), "positive": (1.0, -1.0), "negative": (-1.0, 1.0)}
R = 10_000
N_REFERENCE = 700
CURVE_NS = (100, 200, 400, 800, 1200, 1600, 2400, 3200)
BATCH = 250
BASE_SEED = 20261118

def expit(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))

def transition_probabilities(alpha01: float, alpha10: float):
    return expit(B01), expit(B10), expit(B01 + alpha01), expit(B10 + alpha10)

def count_pmf(pi0: float, K: int, p01: float, p10: float) -> np.ndarray:
    """P(sum_{k=1..K} A_k = j), exact DP; A0~Bernoulli(pi0)."""
    s0 = np.zeros(K + 1, dtype=np.float64)
    s1 = np.zeros(K + 1, dtype=np.float64)
    s0[0], s1[0] = 1.0 - pi0, pi0
    for _ in range(K):
        n0 = np.zeros_like(s0)
        n1 = np.zeros_like(s1)
        n0 += s0 * (1.0 - p01) + s1 * p10
        n1[1:] += s0[:-1] * p01 + s1[:-1] * (1.0 - p10)
        s0, s1 = n0, n1
    pmf = s0 + s1
    pmf /= pmf.sum()
    return pmf

def oracle_mu(pi0: float, K: int, p01: float, p10: float) -> float:
    pi = pi0
    total = 0.0
    for _ in range(K):
        pi = p01 + (1.0 - p01 - p10) * pi
        total += pi
    return total / K

def oracle_theta(pi0: float, K: int, alpha01: float, alpha10: float) -> float:
    p01_0, p10_0, p01_1, p10_1 = transition_probabilities(alpha01, alpha10)
    mu0 = oracle_mu(pi0, K, p01_0, p10_0)
    mu1 = oracle_mu(pi0, K, p01_1, p10_1)
    return (LAMBDA1 - LAMBDA0) * (mu1 - mu0)

def draw_arm(rng: np.random.Generator, n_rep: int, n_arm: int,
             pi0: float, K: int, alpha01: float, alpha10: float,
             lam: float) -> np.ndarray:
    p01_0, p10_0, p01_1, p10_1 = transition_probabilities(alpha01, alpha10)
    pmf0 = count_pmf(pi0, K, p01_0, p10_0)
    pmf1 = count_pmf(pi0, K, p01_1, p10_1)
    mu0 = float(np.dot(np.arange(K + 1) / K, pmf0))
    mu1 = float(np.dot(np.arange(K + 1) / K, pmf1))
    assert abs(mu0 - oracle_mu(pi0, K, p01_0, p10_0)) < 1e-12
    assert abs(mu1 - oracle_mu(pi0, K, p01_1, p10_1)) < 1e-12
    is_d1 = rng.random((n_rep, n_arm)) < lam
    u = rng.random((n_rep, n_arm))
    counts0 = np.searchsorted(np.cumsum(pmf0), u, side="right")
    counts1 = np.searchsorted(np.cumsum(pmf1), u, side="right")
    return np.where(is_d1, counts1, counts0).astype(np.float64) / K

def wilson(successes: int, n: int, z: float = 1.959963984540054):
    phat = successes / n
    den = 1.0 + z*z/n
    center = (phat + z*z/(2*n)) / den
    half = z * math.sqrt(phat*(1-phat)/n + z*z/(4*n*n)) / den
    return center-half, center+half

def run_cell(N: int, pi0: float, K: int, scenario: str, R: int, seed: int):
    if N % 2:
        raise ValueError("N must be even for balanced 1:1 assignment")
    a01, a10 = SCENARIOS[scenario]
    theta = oracle_theta(pi0, K, a01, a10)
    n_arm = N // 2
    rng = np.random.default_rng(seed)
    rejections = covered = 0
    est_all, se_all, width_all = [], [], []
    remaining = R
    while remaining:
        b = min(BATCH, remaining)
        y0 = draw_arm(rng, b, n_arm, pi0, K, a01, a10, LAMBDA0)
        y1 = draw_arm(rng, b, n_arm, pi0, K, a01, a10, LAMBDA1)
        m0, m1 = y0.mean(axis=1), y1.mean(axis=1)
        v0, v1 = y0.var(axis=1, ddof=1), y1.var(axis=1, ddof=1)
        est = m1 - m0
        se2 = v1/n_arm + v0/n_arm
        se = np.sqrt(se2)
        df = se2**2 / ((v1/n_arm)**2/(n_arm-1) + (v0/n_arm)**2/(n_arm-1))
        crit = student_t.ppf(0.975, df)
        lo, hi = est-crit*se, est+crit*se
        valid = np.isfinite(se) & (se > 0) & np.isfinite(df)
        reject = valid & ((lo > 0) | (hi < 0))
        cover = valid & (lo <= theta) & (theta <= hi)
        rejections += int(reject.sum())
        covered += int(cover.sum())
        est_all.append(est); se_all.append(se); width_all.append(hi-lo)
        remaining -= b
    est = np.concatenate(est_all)
    se = np.concatenate(se_all)
    widths = np.concatenate(width_all)
    phat, chat = rejections/R, covered/R
    sampling_sd = float(est.std(ddof=1))
    bias_mcse = float(est.std(ddof=1) / math.sqrt(R))
    squared_error = (est - theta) ** 2
    rmse = float(np.sqrt(np.mean(squared_error)))
    rmse_mcse = float(squared_error.std(ddof=1) / math.sqrt(R) / (2.0 * rmse)) if rmse > 0 else 0.0
    width_mcse = float(widths.std(ddof=1) / math.sqrt(R))
    return {
        "N": N, "R": R, "pi0": pi0, "K": K, "scenario": scenario,
        "alpha01": a01, "alpha10": a10, "lambda0": LAMBDA0, "lambda1": LAMBDA1,
        "theta_true": theta, "rejection_rate": phat,
        "rejection_mcse": math.sqrt(phat*(1-phat)/R),
        "rejection_wilson_low": wilson(rejections,R)[0],
        "rejection_wilson_high": wilson(rejections,R)[1],
        "coverage": chat, "coverage_mcse": math.sqrt(chat*(1-chat)/R),
        "coverage_wilson_low": wilson(covered,R)[0],
        "coverage_wilson_high": wilson(covered,R)[1],
        "bias": float(est.mean()-theta), "bias_mcse": bias_mcse,
        "bias_mcse_over_sampling_sd": bias_mcse / sampling_sd if sampling_sd > 0 else 0.0,
        "rmse": rmse, "rmse_mcse": rmse_mcse,
        "rmse_mcse_over_sampling_sd": rmse_mcse / sampling_sd if sampling_sd > 0 else 0.0,
        "mean_ci_width": float(widths.mean()), "mean_ci_width_mcse": width_mcse,
        "mean_ci_width_mcse_relative": width_mcse / float(widths.mean()) if float(widths.mean()) > 0 else 0.0,
        "mean_se": float(se.mean()),
        "seed": seed, "invalid_replicates": int((~np.isfinite(se) | (se<=0)).sum()),
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path("p178_output"))
    ap.add_argument("--replications", type=int, default=R)
    ap.add_argument("--reference-only", action="store_true")
    args=ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    results=[]; idx=0
    for K in K_VALUES:
        for pi0 in PI_VALUES:
            for scenario in ("null","positive","negative"):
                results.append(run_cell(N_REFERENCE,pi0,K,scenario,args.replications,BASE_SEED+29*idx))
                idx+=1
    extra_fields={"bias_mcse","bias_mcse_over_sampling_sd","rmse_mcse","rmse_mcse_over_sampling_sd","mean_ci_width_mcse","mean_ci_width_mcse_relative"}
    main_fields=[k for k in results[0] if k not in extra_fields]
    with (args.out/"p178_reference_N700.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=main_fields); w.writeheader(); w.writerows([{k:x[k] for k in main_fields} for x in results])
    curve=[]
    if not args.reference_only:
        SCENARIOS["weak_signal"]=(1.0,0.99)
        for n_idx,N in enumerate(CURVE_NS):
            for scenario in ("null","positive","negative","weak_signal"):
                seed=BASE_SEED+100_000+101*n_idx+{"null":0,"positive":1,"negative":2,"weak_signal":3}[scenario]
                curve.append(run_cell(N,0.50,10,scenario,args.replications,seed))
        with (args.out/"p178_central_N_theta_curve.csv").open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=main_fields); w.writeheader(); w.writerows([{k:x[k] for k in main_fields} for x in curve])
    diagnostic_fields=["N","R","pi0","K","scenario","theta_true","bias_mcse","bias_mcse_over_sampling_sd","rmse_mcse","rmse_mcse_over_sampling_sd","mean_ci_width_mcse","mean_ci_width_mcse_relative"]
    diagnostics=[{k:x[k] for k in diagnostic_fields} for x in results+curve]
    with (args.out/"p178_continuous_mcse_diagnostics.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=diagnostic_fields); w.writeheader(); w.writerows(diagnostics)
    script_path=Path(__file__).resolve()
    meta={
        "protocol":"TGCV-C10-S-P178-FOCAL-MC-REPRO-001",
        "python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,
        "rng":"numpy.random.default_rng / PCG64","R_per_cell":args.replications,
        "assignment":"balanced 1:1, independent UE; N total even",
        "parameters":{"lambda0":LAMBDA0,"lambda1":LAMBDA1,"b01":B01,"b10":B10,
                      "baseline_transition_p01":expit(B01),"baseline_transition_p10":expit(B10),
                      "pi0_grid":PI_VALUES,"K_grid":K_VALUES,"scenarios":SCENARIOS},
        "reference_seed_rule":"20261118 + 29*index; index order K={2,10,50}, pi0={.2,.5,.8}, scenario={null,positive,negative}",
        "central_curve_N":CURVE_NS,"central_curve_pi0":0.5,"central_curve_K":10,
        "method":"exact DP marginal pmf for Q_B1 per UE; independent sampling of Q values; Welch two-sample t CI; two-sided alpha=.05",
        "script_sha256":hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "outputs":["p178_reference_N700.csv"]+([] if args.reference_only else ["p178_central_N_theta_curve.csv"])+["p178_continuous_mcse_diagnostics.csv"],
        "limitation":"benchmark estimator only; no TGCV Analyzer, no adversarial measurement scenarios, no confirmatory experiment"
    }
    meta_path=args.out/"p178_run_manifest.json"
    meta_path.write_text(json.dumps(meta,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    meta["sha256"]={name:hashlib.sha256((args.out/name).read_bytes()).hexdigest() for name in meta["outputs"]}
    meta_path.write_text(json.dumps(meta,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"cells_reference":len(results),"cells_curve":len(curve),"out":str(args.out),"manifest":str(meta_path)},indent=2))

if __name__=="__main__": main()
