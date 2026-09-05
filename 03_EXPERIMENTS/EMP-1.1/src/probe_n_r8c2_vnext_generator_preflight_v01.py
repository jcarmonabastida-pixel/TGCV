"""N-R8-C2 vNext generator preflight.

Validates the preparation layer without generating or accepting the 5,000-pair
corpus and without running the scientific experiment.
"""
from __future__ import annotations

import ast
import json
import random
from pathlib import Path

from branch_n_r8_operationalisation_v01 import canonical_state
from branch_n_r8c2_vnext_generator_v01 import (
    GENERATOR if False else CONFIG_PATH,
)
