from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class FigureTarget:
    label: str
    description: str
    notes: str = ""


@dataclass(frozen=True)
class TableTarget:
    label: str
    description: str
    notes: str = ""


FIGURE_TARGETS: List[FigureTarget] = [
    FigureTarget(
        label="F1",
        description="Primary cosmographic constraint plot(s) from legacy data combinations",
        notes="Replace with actual paper figure mapping once extracted."
    ),
    FigureTarget(
        label="F2",
        description="Reconstructed q(z) or equivalent kinematic history plot",
        notes="Verify exact panel composition from paper."
    ),
]

TABLE_TARGETS: List[TableTarget] = [
    TableTarget(
        label="T1",
        description="Best-fit cosmographic parameters for data combinations",
        notes="Needs exact column structure from paper."
    ),
]