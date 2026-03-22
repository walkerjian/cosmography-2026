"""Cosmographic series expansions.

Implement *exactly* the paper’s expressions first (baseline mode),
then add alternative approximants in separate functions/modules.
"""
from __future__ import annotations
import numpy as np
from .constants import C_KM_S

def dL_series_z(z: np.ndarray, h: float, q0: float, j0: float, s0: float, l0: float) -> np.ndarray:
    """Luminosity distance d_L(z) series (baseline Taylor), in Mpc.

    NOTE: This is a stub. Replace with the exact coefficients from the paper.
    """
    z = np.asarray(z, dtype=float)
    H0 = 100.0 * h  # km/s/Mpc
    # Leading term: c z / H0
    return (C_KM_S / H0) * z

def dL_series_y(y: np.ndarray, h: float, q0: float, j0: float, s0: float, l0: float) -> np.ndarray:
    """Luminosity distance d_L(y) series (baseline Taylor in y), in Mpc.

    NOTE: Stub. Replace with paper expression.
    """
    y = np.asarray(y, dtype=float)
    H0 = 100.0 * h
    return (C_KM_S / H0) * y
