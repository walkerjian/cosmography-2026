"""Coordinate transforms (z <-> y and related utilities)."""
import numpy as np

def z_to_y(z: np.ndarray) -> np.ndarray:
    """y = z / (1 + z)"""
    z = np.asarray(z)
    return z / (1.0 + z)

def y_to_z(y: np.ndarray) -> np.ndarray:
    """z = y / (1 - y)"""
    y = np.asarray(y)
    return y / (1.0 - y)
