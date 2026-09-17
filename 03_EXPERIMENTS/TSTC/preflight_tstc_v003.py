"""TGCV WP2 TSTC Fixture-003 preflight runner.

Preflight only. No TSTC trajectory execution is performed.
"""
from tstc_fixture_engine_v003 import run_preflight


def main():
    result = run_preflight()
    assert result["mode"] == "PREFLIGHT_ONLY"
    assert result["engine_version"] == "TSTC_FIXTURE_ENGINE_v003"
    assert len(result["results"]) == 3
    assert all(r["status"] == "PREFLIGHT_PASS" for r in result["results"])
    assert all(r["fixture"]["fixture_version"] == "003" for r in result["results"])
    assert "c03.modify_repo" in result["results"][1]["fixture"]["U_tau"]
    print("TSTC_FIXTURE_003_PREFLIGHT_STATUS=PREFLIGHT_PASS")
    for r in result["results"]:
        print(f'{r["fixture"]["fixture_id"]}=PREFLIGHT_PASS')
        print(f'ruleset_hash={r["ruleset_hash"]}')
        print(f'output_hash={r["output_hash"]}')


if __name__ == "__main__":
    main()
