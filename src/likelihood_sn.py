"""Supernova likelihood.

Baseline should implement the paper’s nuisance-parameter minimization/marginalisation.
"""
import numpy as np

def chi2_sn_marginalized(mu_obs, mu_th, cov):
    """Stub: replace with the paper’s A,B,C marginalization form."""
    r = mu_obs - mu_th
    return float(r.T @ np.linalg.inv(cov) @ r)
