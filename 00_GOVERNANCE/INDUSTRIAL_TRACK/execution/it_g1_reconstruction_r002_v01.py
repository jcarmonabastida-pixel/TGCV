#!/usr/bin/env python3
"""R002 launcher for IT-G1 independent reconstruction.
Run in an isolated executor context after receiving only the frozen package.
No AWS calls are made by this launcher or by the reconstruction engine.
"""
from pathlib import Path
import runpy
import sys

ENGINE = Path(__file__).with_name("it_g1_independent_reconstruction_executor_v01.py")
repo = Path(__file__).resolve().parents[3]
out = repo / "03_EXPERIMENTS" / "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE" / "R002" / "IT-G1_R002_RECONSTRUCTION_001.json"
sys.argv = [str(ENGINE), "--reconstruction-id", "R002", "--executor-id", "IT-G1-R002-EXECUTOR-0.1", "--repo-root", str(repo), "--output", str(out)]
runpy.run_path(str(ENGINE), run_name="__main__")
