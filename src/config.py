"""Central configuration.

This file is the single source of truth for:
- baseline (2012) priors/constants
- file paths for datasets
- run settings (sampler, thinning, burn-in)
- reproduction mode switches and dataset flags

Populate and refine this from `notebooks/00_paper_archaeology.ipynb`.
"""
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
OUTPUT_DIR = ROOT / "outputs"


@dataclass(frozen=True)
class PathConfig:
    """Filesystem layout for the project."""

    root: Path = ROOT
    data: Path = DATA_DIR
    docs: Path = DOCS_DIR
    outputs: Path = OUTPUT_DIR

    legacy: Path = DATA_DIR / "legacy"
    modern: Path = DATA_DIR / "modern"

    union2: Path = DATA_DIR / "legacy" / "union2"
    grb_legacy: Path = DATA_DIR / "legacy" / "grb"
    bao_legacy: Path = DATA_DIR / "legacy" / "bao"
    cmb_legacy: Path = DATA_DIR / "legacy" / "cmb"
    hz_legacy: Path = DATA_DIR / "legacy" / "hz"

    pantheon_plus: Path = DATA_DIR / "modern" / "pantheon_plus"
    bao_modern: Path = DATA_DIR / "modern" / "bao"
    hz_modern: Path = DATA_DIR / "modern" / "hz"
    grb_modern: Path = DATA_DIR / "modern" / "grb"


@dataclass(frozen=True)
class BaselinePriors:
    """Paper-era priors/constants for faithful baseline reproduction.

    These defaults preserve the values currently captured from the scaffold.
    Replace or extend only when the archaeology notebook confirms exact usage.
    """

    # TODO: confirm exact H0 prior source and whether h or H0 is sampled directly.
    h_mean: float = 0.742
    h_sigma: float = 0.036

    # TODO: confirm whether this enters directly as a Gaussian prior or via a derived CMB term.
    omega_m_h2_mean: float = 0.1356
    omega_m_h2_sigma: float = 0.0034

    # TODO: confirm precise definition and covariance treatment of the shift parameter.
    shift_R_mean: float = 1.725
    shift_R_sigma: float = 0.019

    # Broad hard bounds for sampled cosmographic parameters.
    h_bounds: Tuple[float, float] = (0.5, 0.9)
    q0_bounds: Tuple[float, float] = (-5.0, 1.0)
    j0_bounds: Tuple[float, float] = (-10.0, 10.0)
    s0_bounds: Tuple[float, float] = (-100.0, 100.0)
    l0_bounds: Tuple[float, float] = (-500.0, 500.0)


@dataclass(frozen=True)
class CosmographySettings:
    """Model-expansion settings for baseline and later comparisons."""

    redshift_variable: str = "y"  # Allowed: "z", "y"
    max_order: int = 5
    c_km_s: float = 299792.458


@dataclass(frozen=True)
class SamplerSettings:
    """Paper-like sampling defaults.

    Adjust only after baseline reproduction is working and documented.
    """

    method: str = "mcmc"
    n_chains: int = 8
    n_steps: int = 100_000
    burn_in_frac: float = 0.30
    thin: int = 10  # TODO: confirm paper’s thinning practice
    random_seed: int = 42


@dataclass(frozen=True)
class DataFlags:
    """Dataset inclusion switches for controlled reproduction runs."""

    use_union2: bool = True
    use_grb: bool = True
    use_bao: bool = True
    use_cmb: bool = True
    use_hz: bool = True


@dataclass(frozen=True)
class ReproductionConfig:
    """Top-level configuration object for the project."""

    paper_id: str = "capozziello_2012_high_redshift_cosmography"
    baseline_mode: str = "legacy_data_original_method"
    paths: PathConfig = field(default_factory=PathConfig)
    priors: BaselinePriors = field(default_factory=BaselinePriors)
    cosmography: CosmographySettings = field(default_factory=CosmographySettings)
    sampler: SamplerSettings = field(default_factory=SamplerSettings)
    data_flags: DataFlags = field(default_factory=DataFlags)


CONFIG = ReproductionConfig()
PRIOR = CONFIG.priors
SAMPLER = CONFIG.sampler
PATHS = CONFIG.paths

# Backward-compatible aliases for early scaffold code.
DOCS_DIR = PATHS.docs
