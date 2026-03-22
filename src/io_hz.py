"""IO for H(z) datasets (legacy Stern et al. 2010 and modern compilations)."""
from pathlib import Path
import pandas as pd

def load_hz_table(path: Path) -> pd.DataFrame:
    """Expect columns: z, Hz, sigma_Hz."""
    return pd.read_csv(path)
