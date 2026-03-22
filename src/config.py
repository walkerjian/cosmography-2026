"""Central configuration.

This file is the single source of truth for:
- baseline (2012) priors/constants
- file paths for datasets
- run settings (sampler, thinning, burn-in)

Populate this from `notebooks/00_paper_archaeology.ipynb`.
"""
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

@dataclass(frozen=True)
class BaselinePriors:
    # TODO: fill with exact values from the paper
    h_mean: float = 0.742
    h_sigma: float = 0.036
    omega_m_h2_mean: float = 0.1356
    omega_m_h2_sigma: float = 0.0034
    shift_R_mean: float = 1.725
    shift_R_sigma: float = 0.019

@dataclass(frozen=True)
class SamplerSettings:
    # Paper-like settings (adjust only after baseline reproduction)
    n_chains: int = 8
    n_steps: int = 100_000
    burn_in_frac: float = 0.30
    thin: int = 10  # TODO: confirm paper’s thinning practice

PRIOR = BaselinePriors()
SAMPLER = SamplerSettings()

DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"
