"""Preflight-only harness for the frozen Fixture-002 TSTC engine."""
from tstc_fixture_engine_v002 import run_preflight


def main():
    result = run_preflight()
    assert result["mode"] == "PREFLIGHT_ONLY"
    assert len(result["results"]) == 3
    assert all(r["status"] == "PREFLIGHT_PASS" for r in result["results"])
    print("TSTC_FIXTURE_002_PREFLIGHT_STATUS=PREFLIGHT_PASS")
    for r in result["results"]:
        print(f'{r["fixture"]["fixture_id"]}=PREFLIGHT_PASS')


if __name__ == "__main__":
    main()
