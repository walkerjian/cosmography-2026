# cosmography-2026

Baseline-first reproduction and 2026 update of the 2012 paper:
*High redshift cosmography: new results and implication for dark energy*.

## Philosophy
1. **Reproduce the 2012 analysis faithfully** (same assumptions, priors, data) before changing anything.
2. Update **data only** (method frozen).
3. Update **method** (data fixed) using better-behaved approximants.
4. Run robustness/ablations.

## Quick start
- Create an environment (see `environment.yml`).
- Open notebooks in order: `notebooks/00_paper_archaeology.ipynb` → `01_...` → `02_...`.

## Data
Place legacy and modern datasets under `data/` as indicated by the folder names.
Do not commit large raw data to git; prefer small config + download instructions.
