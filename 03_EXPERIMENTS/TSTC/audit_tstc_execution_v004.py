"""Static pre-execution audit for TSTC execution adapter v004."""
from __future__ import annotations
import ast
from pathlib import Path

TARGET=Path(__file__).with_name("tstc_execution_v004.py")
REQUIRED_FIELDS={"fixture_id","fixture_version","connector_id","intervention_id","S0","C0","L_version","U_tau","T_acc_0","transition","S1","C1","T_acc_1","Delta_T_acc","trajectory","baseline_model","baseline_representation","baseline_reconstruction","comparison_observations","limitations","non_claims","execution_metadata"}
REQUIRED_FUNCTIONS={"run_execution","_record","_negative","_cross_domain","_baseline_actions","_comparison","_trajectory"}
COMPARISON_KEYS={"transformation_identities","admissibility_conditions","state_context_dependencies","transition_causing_accessibility_change","cross_domain_dependency","trajectory_consequence","assumptions","information_omitted"}
REQUIRED_TEXT=("TSTC_EXECUTION_v004","Fixture-003","Independent conventional baseline feasibility functions.","EQUIVALENT_REPRESENTATION","output_hash","source_commit","random_seed","C01_to_C03","C03_to_C05")

def main():
    source=TARGET.read_text(encoding="utf-8"); tree=ast.parse(source,filename=str(TARGET)); failures=[]
    funcs={n.name for n in ast.walk(tree) if isinstance(n,ast.FunctionDef)}
    for f in REQUIRED_FUNCTIONS:
        if f not in funcs: failures.append("MISSING_FUNCTION:"+f)
    for text in REQUIRED_TEXT:
        if text not in source: failures.append("MISSING_REQUIRED_TEXT:"+text)
    for field in REQUIRED_FIELDS:
        if f'"{field}"' not in source: failures.append("MISSING_SCHEMA_FIELD:"+field)
    for key in COMPARISON_KEYS:
        if f'"{key}"' not in source: failures.append("MISSING_COMPARISON_DIMENSION:"+key)
    if 'f.fixture_id.replace("FX-","")' not in source: failures.append("MISSING_CONNECTOR_ID_DERIVATION")
    if 'assert tuple(tg0)==bb and tuple(tg1)==ba' not in source: failures.append("MISSING_BASELINE_PARITY_GUARD")
    if 'assert delta["changed"]==() and delta["opened"]==() and delta["closed"]==()' not in source: failures.append("MISSING_NEGATIVE_CONTROL_GUARD")
    if 'assert "c03.modify_repo" in c03_0 and "c03.modify_repo" not in c03_1' not in source: failures.append("MISSING_C01_C03_DENIED_GUARD")
    if 'assert "c05.redirect_A_to_B" in c05_0 and "c05.redirect_A_to_B" not in c05_1' not in source: failures.append("MISSING_C03_C05_PROPAGATION_GUARD")
    if 'result["execution_metadata"]["output_hash"]=digest(result)' not in source: failures.append("MISSING_COMPLETE_OUTPUT_HASH_STEP")
    if failures:
        print("TSTC_EXECUTION_V004_STATIC_AUDIT=BLOCKED")
        for x in failures: print(x)
        raise SystemExit(1)
    print("TSTC_EXECUTION_V004_STATIC_AUDIT=PASS")
    print("NO_TSTC_EXECUTION_PERFORMED=True")

if __name__=="__main__": main()
