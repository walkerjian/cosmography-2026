"""Observable-layer functions: distance modulus, H(z), BAO summaries, etc."""
from __future__ import annotations
import numpy as np
from .cosmography_series import dL_series_z, dL_series_y

def mu_from_dL_mpc(dL_mpc: np.ndarray) -> np.ndarray:
    """Distance modulus from luminosity distance in Mpc: μ = 5 log10(dL/Mpc) + 25."""
    dL_mpc = np.asarray(dL_mpc, dtype=float)
    return 5.0 * np.log10(dL_mpc) + 25.0

def mu_theory(z: np.ndarray, params: dict, mode: str = "z") -> np.ndarray:
    """Theory μ(z) using either z-series or y-series."""
    z = np.asarray(z, dtype=float)
    if mode == "z":
        dL = dL_series_z(z, **params)
    elif mode == "y":
        y = z / (1.0 + z)
        dL = dL_series_y(y, **params)
    else:
        raise ValueError("mode must be 'z' or 'y'")
    return mu_from_dL_mpc(dL)
