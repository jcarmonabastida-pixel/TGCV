import json

def oracle_expected():
    return {
      "persistence": "PERSISTENCE",
      "expansion": "EXPANSION",
      "contraction": "CONTRACTION",
      "reconfiguration": "RECONFIGURATION_ONLY",
      "representation_renaming": "INVARIANT",
      "structural_null": "PERSISTENCE",
      "state_only_variation": "NO_OMEGA_CHANGE",
      "structural_change_fixed_state": "STRUCTURAL_CHANGE_DETECTED",
      "incomparable": "NON_COMPARABLE",
      "conditional_H0": "NO_REORGANIZATION",
      "conditional_H1": "CONDITIONAL_REORGANIZATION"
    }

if __name__=="__main__":
    print(json.dumps(oracle_expected(),sort_keys=True,separators=(",",":")))
