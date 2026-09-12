#!/usr/bin/env python3
"""R001 launcher for IT-G1 independent reconstruction.
Run from the TGCV repository root after obtaining the frozen canonical package.
No AWS calls are made by this launcher or by the reconstruction engine.
"""
from pathlib import Path
import runpy
import sys

ENGINE = Path(__file__).with_name("it_g1_independent_reconstruction_executor_v01.py")
repo = Path(__file__).resolve().parents[3]
out = repo / "03_EXPERIMENTS" / "IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE" / "R001" / "IT-G1_R001_RECONSTRUCTION_001.json"
sys.argv = [str(ENGINE), "--reconstruction-id", "R001", "--executor-id", "IT-G1-R001-EXECUTOR-0.1", "--repo-root", str(repo), "--output", str(out)]
runpy.run_path(str(ENGINE), run_name="__main__")
