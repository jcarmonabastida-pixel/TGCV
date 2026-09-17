from pathlib import Path
import hashlib

current = Path('00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md')
v14 = Path('00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.14.md')
v15 = Path('00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.15.md')
pointer = Path('00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md')
workflow = Path('.github/workflows/reconstruct-v115.yml')
trigger = Path('.v115_reconstruction_trigger')

base = v14.read_text(encoding='utf-8')
alias = current.read_text(encoding='utf-8')
assert base == alias, 'BASE_INTEGRITY_FAIL'
assert base.startswith('# TGCV — Evidence-to-Claim Matrix — Current v1.14'), 'BASE_VERSION_FAIL'
assert not v15.exists(), 'REFUSE_OVERWRITE_EXISTING_V15'
marker = '## Matrix preservation rule'
assert marker in base, 'PRESERVATION_MARKER_MISSING'
body = base.split(marker, 1)[1]
header = '''# TGCV — Evidence-to-Claim Matrix — Current v1.15

**Status:** GOVERNANCE CONTROL ARTIFACT — CURRENT  
**Date:** 2026-09-18  
**Predecessor:** v1.14  
**Incremental governance update:** Adds the C05 EV–Grid Minimum Demonstrator material evidence record and bounded propagation to C02, C07, C08 and C16. No claim-level status/level is changed; C09 remains unchanged.

**C05 material-evidence update:** The C05 frozen runner, runtime execution, post-execution audit and evidence-to-claim propagation are incorporated as a bounded synthetic application-fit record. The result is propagated only to C02, C07, C08 and C16 within the explicitly stated methodological limits. The synthetic baseline is not independent evidence, and NC2 does not constitute a trajectory-policy sensitivity test because the frozen trajectory implementation does not consume the added `selection_tiebreak` field.

'''
text = header + marker + body
additions = {
'C02': ' C05 adds bounded synthetic application-fit evidence for explicit candidate transformations, admissibility/accessibility and `T_acc`, including the T3 `T_acc` reduction from 8 to 6; baseline equivalence is not independent evidence and no claim-level upgrade is inferred.',
'C07': ' C05 adds bounded synthetic evidence of `Delta T_acc != 0` under T3 (8→6, with `accept_B` and `redirect_A_to_B` closed) and no accessibility delta under T1/T2/T4/T5/T6/NC1/NC2; this is synthetic methodological evidence only.',
'C08': ' C05 adds bounded synthetic transition/trajectory representation; NC2 is not a trajectory-policy sensitivity test because `trajectory()` does not consume `selection_tiebreak`; no causal trajectory estimand is established.',
'C16': ' C05 adds bounded synthetic application-fit evidence preserving the distinctions among candidate transformations, admissibility, `T_acc`, transition, bounded trajectory fields, negative controls and explicit non-claims; no causal, value, superiority, generality or deployment claim is inferred.'}
lines = text.splitlines(); out=[]; changed=set()
for line in lines:
    if line.startswith('| C') and line.count('|') >= 6:
        parts=line.split('|'); cid=parts[1].strip()
        if cid in additions:
            parts[5]=parts[5].rstrip()+additions[cid]
            line='|'.join(parts); changed.add(cid)
    out.append(line)
assert changed == set(additions), f'CLAIM_ROUTING_FAIL:{sorted(changed)}'
text='\n'.join(out)+'\n'
c05='''
## Material empirical evidence — C05 EV–Grid Minimum Demonstrator v001

**Case:** `C05_EV_GRID_SYNTHETIC_MINIMUM_DEMONSTRATOR_V001`  
**Status:** `EXECUTION COMPLETE — PASS WITH METHODOLOGICAL LIMITATIONS`  
**Runner:** `03_EXPERIMENTS/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_MINIMUM_DEMONSTRATOR_V001.py`  
**Runner commit:** `e8e55f50f82b9bdf69eeca4d48deb9d23799672e`  
**SPEC_COMMIT:** `5aa2c7e20ea3f5775b2d6e60797f9be9efe10e05`  
**FIXTURE_COMMIT:** `9dd6e9b6bb8d0b7a7e686c4dc61926fc627fa8b6`  
**Execution:** `C05_EXECUTION_COMPLETE`  
**Python:** `3.8.10`  
**Platform:** `Windows-10-10.0.26200-SP0`  
**Output hash:** `27025e638c05458e19a125c00d9d86d89906bc418eec5670eddec14c89e96880`  
**Preflight:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_RUNNER_PREFLIGHT_001.md`  
**Post-execution audit:** `00_GOVERNANCE/SIP/TGCV_APPLICATION_FIT_WP2_C05_EV_GRID_POST_EXECUTION_AUDIT_001.md`

The frozen synthetic demonstrator evaluates explicit candidate transformations, admissibility, accessibility and bounded transition/trajectory fields. Under T3, `T_acc` changes from 8 to 6, closing `accept_B` and `redirect_A_to_B`. T1, T2, T4, T5, T6, NC1 and NC2 show no accessibility delta in the frozen execution.

This is bounded synthetic methodological/application-fit evidence only. The implementation's `baseline(s,c,l)` returns `admissible(s,c,l)`, so `baseline_equivalent=true` is not independent baseline evidence. NC2 specifies `selection_tiebreak=reverse_lexical`, but `trajectory()` does not consume this field; therefore NC2 is not a trajectory-policy sensitivity test. No causal validity, generality, value/ROI, superiority, deployment readiness or claim-level upgrade is inferred.

**Claim routing:** C02, C07, C08, C16 only.
'''
text += c05

# Verify cumulative preservation. The four routed rows are intentionally modified only in column 5 (Evidence impact).
base_lines = base.split(marker,1)[1].splitlines()
new_lines = text.splitlines()
new_rows = {r.split('|')[1].strip(): r.split('|') for r in new_lines if r.startswith('| C') and r.count('|') >= 6}
base_rows = {r.split('|')[1].strip(): r.split('|') for r in base_lines if r.startswith('| C') and r.count('|') >= 6}
assert set(base_rows) == set(new_rows) and len(new_rows)==16, 'CLAIM_ROW_SET_FAIL'
for cid, brow in base_rows.items():
    nrow = new_rows[cid]
    assert len(brow)==8 and len(nrow)==8, 'ROW_SCHEMA_FAIL'
    if cid in additions:
        assert nrow[1:5] == brow[1:5], f'ROW_PRESERVATION_FAIL:{cid}:left'
        assert nrow[6:8] == brow[6:8], f'ROW_PRESERVATION_FAIL:{cid}:right'
        assert nrow[5].startswith(brow[5]), f'ROW_PRESERVATION_FAIL:{cid}:impact'
    else:
        assert nrow == brow, f'ROW_UNCHANGED_FAIL:{cid}'
# All non-table inherited lines must survive verbatim.
base_nonrows=[ln for ln in base_lines if not (ln.startswith('| C') and ln.count('|')>=6)]
for ln in base_nonrows:
    if ln.strip() and ln not in new_lines: raise AssertionError('CUMULATIVE_CONTENT_FAIL:'+ln[:160])

rows=[ln for ln in new_lines if ln.startswith('| C') and ln.count('|')>=6]
assert len(rows)==16, f'CLAIM_COUNT_FAIL:{len(rows)}'
assert all(len(r.split('|'))==8 for r in rows), 'COLUMN_COUNT_FAIL'
assert text.count('## Material empirical evidence') == base.count('## Material empirical evidence')+1, 'MATERIAL_SECTION_COUNT_FAIL'
for cid in ('C02','C07','C08','C16'):
    assert 'C05 adds bounded' in next(r for r in rows if r.startswith('| '+cid+' |'))
for cid in ('C01','C03','C04','C05','C06','C09','C10','C11','C12','C13','C14','C15'):
    assert 'C05 adds bounded' not in next(r for r in rows if r.startswith('| '+cid+' |'))
p=pointer.read_text(encoding='utf-8'); assert '**Current version:** v1.15' not in p
v15.write_text(text,encoding='utf-8'); current.write_text(text,encoding='utf-8')
pointer.write_text('''# TGCV — Evidence-to-Claim Matrix — CURRENT POINTER

**Status:** CURRENT CONTROL POINTER  
**Current matrix:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md`  
**Current version:** v1.15  
**Versioned artifact:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.15.md`  
**Predecessor:** v1.14  
**Established:** 2026-09-18

v1.15 cumulatively preserves v1.14 and adds only the C05 EV–Grid Minimum Demonstrator material evidence record and bounded propagation to C02, C07, C08 and C16. No claim-level status/level changes; C09 remains unchanged.
''',encoding='utf-8')
assert current.read_text(encoding='utf-8') == v15.read_text(encoding='utf-8'), 'ALIAS_V15_MISMATCH'
print('VERIFICATION_PASS'); print('claim_rows=',len(rows)); print('material_sections=',text.count('## Material empirical evidence')); print('sha256=',hashlib.sha256(text.encode()).hexdigest())
workflow.unlink(); trigger.unlink()
