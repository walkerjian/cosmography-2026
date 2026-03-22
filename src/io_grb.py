"""IO for GRB Hubble diagram inputs (legacy calibrated Amati / LX-Ta)."""
from pathlib import Path
import pandas as pd

def load_grb_hd(path: Path) -> pd.DataFrame:
    """Expect columns: z, mu, sigma_mu (or full covariance)."""
    return pd.read_csv(path)
