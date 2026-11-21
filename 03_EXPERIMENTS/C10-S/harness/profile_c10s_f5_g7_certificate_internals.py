"""Single M30/R20 resource-only profile of exact F5 certificate internals."""
from __future__ import annotations
import json, resource, time
from collections import Counter
from pathlib import Path

import c10s_f5_rational_score_polynomials as rational
import c10s_fitted_beta_binomial_bootstrap as fitted
import c10s_f5_beta_binomial_likelihood_diagnostics as diagnostic
import c10s_nested_mr_comparative_inference_engine as engine
import run_c10s_f5_g7_tiera_calibration as g7

CELL = "F5_beta22_M30_R20"

def summarize(name, result, observations):
    if not isinstance(result, dict): return
    keys = {
        "beta_binomial_global_mle_certificate": ("status","refinement_history"),
        "beta_binomial_compactified_stationary_census": ("status","interval_first_attempt","concentration_resultant","concentration_projection"),
        "conditional_mean_adaptive_concentration_census": ("status","processed_intervals","subdivisions","krawczyk_attempts","excluded_intervals","certified_simple_root_intervals","unresolved_intervals"),
        "conditional_mean_tube_and_concentration_exclusion": ("status","t_bounds","mean_root_tube_mu_bounds"),
        "krawczyk_certify_unique_root": ("status","root_box","krawczyk_box"),
        "_beta_binomial_likelihood_enclosure": ("status","likelihood_bounds"),
    }.get(name, ())
    if keys:
        row = {"function":name}
        for key in keys:
            value = result.get(key)
            if key in ("excluded_intervals","certified_simple_root_intervals","unresolved_intervals") and isinstance(value,list):
                row[key+"_count"] = len(value)
            elif key == "refinement_history" and isinstance(value,list):
                row[key] = [{"refinement":v.get("refinement"),"status":v.get("census_status")} for v in value]
            elif key == "interval_first_attempt" and isinstance(value,dict):
                row[key] = {k:value.get(k) for k in ("status","processed_intervals","subdivisions","krawczyk_attempts")}
            else:
                row[key] = value
        observations.append(row)

def profile(output: Path):
    timings = Counter()
    calls = Counter()
    stack = []
    observations = []
    current = {"dataset":CELL}

    def wrap(module, name):
        original = getattr(module,name)
        def measured(*args,**kwargs):
            started=time.perf_counter()
            frame={"name":name,"child":0.0}
            stack.append(frame)
            try:
                result=original(*args,**kwargs)
                summarize(name,result,observations)
                return result
            finally:
                elapsed=time.perf_counter()-started
                stack.pop()
                exclusive=max(0.0,elapsed-frame["child"])
                timings[name]+=exclusive
                calls[name]+=1
                if stack: stack[-1]["child"]+=elapsed
        setattr(module,name,measured)

    # Inner-to-outer wrappers; each function is measured exclusively (children removed).
    names = [
      "beta_binomial_score_numerators","compactify_concentration",
      "compactified_axis_common_components","beta_binomial_boundary_likelihoods",
      "beta_binomial_joint_corner_likelihood_limits",
      "_strip_axis_content_factors_outside_open_unit_domain",
      "bernstein_coefficients_on_box","krawczyk_certify_unique_root",
      "conditional_mean_tube_and_concentration_exclusion",
      "conditional_mean_adaptive_concentration_census",
      "beta_binomial_compactified_stationary_census",
      "_beta_binomial_likelihood_enclosure","beta_binomial_global_mle_certificate",
    ]
    for name in names:
        if hasattr(rational,name): wrap(rational,name)
    # fitted module imported the certificate by name before instrumentation.
    fitted.beta_binomial_global_mle_certificate = rational.beta_binomial_global_mle_certificate

    # Track but do not optimize/skip diagnostic work: this remains an end-to-end dataset profile.
    def wrap_simple(module,name,label):
        original=getattr(module,name)
        def measured(*args,**kwargs):
            start=time.perf_counter()
            try:return original(*args,**kwargs)
            finally:timings[label]+=time.perf_counter()-start;calls[label]+=1
        setattr(module,name,measured)
    wrap_simple(fitted,"minimize","P_optimizer_inclusive")
    wrap_simple(diagnostic,"minimize","A_I_optimizer_inclusive")
    wrap_simple(engine,"_frozen_v002_baseline","C0_baseline")
    wrap_simple(fitted,"_vectorized_bernoulli_bootstrap_components","C5_bootstrap")

    g7.validate_seed_separation()
    spec=next(s for s in g7.f5_specs() if s.cell_id==CELL)
    wall0=time.perf_counter(); cpu0=time.process_time()
    result=g7.run_cell(spec,k=1,c0_b=g7.C0_B,c5_b=g7.C5_B,
                       seed_namespace=g7.RESOURCE_NAMESPACE,adjudicate=False)
    wall=time.perf_counter()-wall0; cpu=time.process_time()-cpu0
    rec=result["records"][0]
    candidate=rec["comparison"]["candidates"][0]["comparison"]
    provenance=dict(candidate.get("provenance",[]))
    payload={
      "schema":"C10S-F5-G7-CERTIFICATE-INTERNAL-PROFILE-001",
      "scope":"ONE_RESOURCE_ONLY_M30_R20_DATASET_NO_HOLDOUT_NO_COVERAGE",
      "seed_namespace":g7.RESOURCE_NAMESPACE,"cell_id":CELL,
      "dataset_id":rec["dataset_id"],"K":1,"C0_B":g7.C0_B,"C5_B":g7.C5_B,
      "wall_seconds":wall,"cpu_seconds":cpu,
      "peak_rss_kib":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      "global_mle_certificate_status":provenance.get("global_mle_certificate_status"),
      "interval_emitted_within":candidate.get("within_interval") is not None,
      "interval_emitted_between":candidate.get("between_interval") is not None,
      "abstention_reason":candidate.get("abstention_reason"),
      "exclusive_component_seconds":dict(timings),
      "component_call_counts":dict(calls),
      "internal_observations":observations,
    }
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(payload,sort_keys=True,indent=2,default=str)+"\\n",encoding="utf-8")
    print(json.dumps(payload,sort_keys=True,indent=2,default=str))
    return payload

def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument("--output",required=True,type=Path)
    a=p.parse_args();profile(a.output);return 0
if __name__=="__main__":raise SystemExit(main())
