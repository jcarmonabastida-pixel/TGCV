"""N-R6.1 prospective learner implementation.

Controlled Branch N reconstruction only. This module does not recover the historical
EMP-1.1 executable and contains no historical result values.
"""
from __future__ import annotations

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier

HGB_PARAMS = {
    "loss": "log_loss", "learning_rate": 0.1, "max_iter": 100,
    "max_leaf_nodes": 31, "max_depth": None, "min_samples_leaf": 20,
    "l2_regularization": 0.0, "max_features": 1.0, "max_bins": 255,
    "categorical_features": None, "early_stopping": "auto", "scoring": "loss",
    "validation_fraction": 0.1, "n_iter_no_change": 10, "tol": 1e-7,
    "random_state": 3100000, "class_weight": None,
}

RF_PARAMS = {
    "n_estimators": 100, "criterion": "gini", "max_depth": None,
    "min_samples_split": 2, "min_samples_leaf": 1, "max_features": "sqrt",
    "bootstrap": True, "class_weight": None, "random_state": 3100000, "n_jobs": 1,
}

B_DIM = 16
R_DIM = 58
BR_DIM = 74
PERMUTATIONS = 200_000
PERMUTATION_SEED = 13_579
ALPHA = 0.05
PRACTICAL_DELTA = 0.04


def make_hgb() -> HistGradientBoostingClassifier:
    return HistGradientBoostingClassifier(**HGB_PARAMS)


def make_random_forest() -> RandomForestClassifier:
    return RandomForestClassifier(**RF_PARAMS)


def fit_primary(X_train: np.ndarray, y_train: np.ndarray) -> HistGradientBoostingClassifier:
    model = make_hgb()
    model.fit(X_train, y_train)
    return model


def predict_logloss(model, X_test: np.ndarray, y_test: np.ndarray) -> np.ndarray:
    p = model.predict_proba(X_test)
    return -np.log(np.clip(p[np.arange(len(y_test)), y_test.astype(int)], 1e-15, 1.0))


def paired_delta(loss_b: np.ndarray, loss_br: np.ndarray) -> np.ndarray:
    a = np.asarray(loss_b, dtype=float)
    b = np.asarray(loss_br, dtype=float)
    if a.shape != b.shape:
        raise ValueError("PAIRED_SHAPE_MISMATCH")
    return a - b


def signflip_pvalue(delta: np.ndarray) -> float:
    """Two-sided finite Monte-Carlo sign-flip p-value."""
    d = np.asarray(delta, dtype=float)
    if d.ndim != 1 or d.size == 0:
        raise ValueError("INVALID_DELTA_VECTOR")
    observed = abs(float(np.mean(d)))
    rng = np.random.default_rng(PERMUTATION_SEED)
    exceed = 0
    for _ in range(PERMUTATIONS):
        signs = rng.integers(0, 2, size=d.size, dtype=np.int8) * 2 - 1
        if abs(float(np.mean(d * signs))) >= observed:
            exceed += 1
    return (exceed + 1) / (PERMUTATIONS + 1)


def evaluate_pair(model_b, model_br, Xb_test, Xbr_test, y_test):
    lb = predict_logloss(model_b, Xb_test, y_test)
    lbr = predict_logloss(model_br, Xbr_test, y_test)
    d = paired_delta(lb, lbr)
    p = signflip_pvalue(d)
    return {
        "base_logloss": float(np.mean(lb)),
        "tgcv_logloss": float(np.mean(lbr)),
        "delta_logloss": float(np.mean(d)),
        "sd_delta": float(np.std(d, ddof=1)),
        "paired_signflip_p": p,
        "meets_practical_delta": bool(np.mean(d) >= PRACTICAL_DELTA),
        "meets_alpha": bool(p < ALPHA),
    }
