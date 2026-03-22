"""IO for Union2 (legacy) supernova sample.

This is intentionally minimal; file formats vary.
Populate after you obtain the exact Union2 data product used in the paper.
"""
from pathlib import Path
import pandas as pd

def load_union2(path: Path) -> pd.DataFrame:
    """Return a dataframe with at least columns: z, mu, sigma_mu (or cov)."""
    raise NotImplementedError("Add Union2 parser once the exact file is pinned down.")
