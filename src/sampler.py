"""Sampling utilities (emcee wrapper).

Keep baseline settings visible and reproducible.
"""
from __future__ import annotations
import numpy as np

def loglike_total(params: dict) -> float:
    raise NotImplementedError

def run_emcee(*args, **kwargs):
    raise NotImplementedError
