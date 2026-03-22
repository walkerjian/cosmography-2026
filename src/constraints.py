"""Physical / numerical constraints used during sampling."""
import numpy as np

def is_physical(dL: np.ndarray, H2: np.ndarray | None = None) -> bool:
    """Basic positivity checks. Extend to match paper’s cuts."""
    if np.any(~np.isfinite(dL)) or np.any(dL <= 0):
        return False
    if H2 is not None:
        if np.any(~np.isfinite(H2)) or np.any(H2 <= 0):
            return False
    return True
