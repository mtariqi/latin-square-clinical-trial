"""
scheduler.py
------------
COMALLS Latin-Square Scheduler for Machine Learning experiments.

This scheduler assigns:
- a model (Condition A)
- two context factors (Condition B and C)

Using a Latin Square to ensure every model appears exactly once
in every (context1 × context2) combination.
"""

from dataclasses import dataclass
from typing import List, Dict, Iterator, Any
from .latin_square import generate_latin_square


@dataclass
class Episode:
    """
    A single scheduled training/evaluation episode in COMALLS.

    Attributes:
        model: Model or model identifier used for this episode.
        context1: First controlled context factor (e.g., domain).
        context2: Second controlled context factor (e.g., noise level).
        episode_id: Integer index for reproducibility.
    """
    model: Any
    context1: Any
    context2: Any
    episode_id: int


class LatinSquareScheduler:
    """
    COMALLS Scheduler.

    Organizes ML experiments using a k × k Latin Square so that each model
    is observed exactly once under every combination of two context factors.

    Example:
    --------
    scheduler = LatinSquareScheduler(
        models=["ResNet", "ViT", "MLP"],
        context1=["low_domain_shift", "medium", "high"],
        context2=["low_noise", "high_noise"],
        seed=42
    )

    for ep in scheduler:
        run_episode(model=ep.model, context1=ep.context1, context2=ep.context2)

    """

    def __init__(
        self,
        models: List[Any],
        context1: List[Any],
        context2: List[Any],
        seed: int | None = None
    ):
        assert len(models) == len(context1), \
            "Latin Square requires |models| = |context1|"

        self.k = len(models)
        self.models = models
        self.context1 = context1
        self.context2 = context2
        self.seed = seed

        # Generate Latin square (k × k)
        self.square = generate_latin_square(self.k, seed=self.seed)

        # Expand to create episodes
        self._episodes = self._build_episodes()

    def _build_episodes(self) -> List[Episode]:
        """
        Build a list of scheduled episodes based on the Latin Square.

        For a square S, S[i][j] = index of model chosen for context pair (i, j).
        i indexes context1 and j indexes context2.
        """
        episodes = []
        episode_id = 0

        for i in range(self.k):
            for j in range(self.k):
                model_idx = self.square[i][j]
                episodes.append(
                    Episode(
                        model=self.models[model_idx],
                        context1=self.context1[i],
                        context2=self.context2[j],
                        episode_id=episode_id
                    )
                )
                episode_id += 1

        return episodes

    def __iter__(self) -> Iterator[Episode]:
        """Iterate through episodes in a reproducible sequence."""
        return iter(self._episodes)

    def to_dataframe(self):
        """Optional convenience shortcut for pandas users."""
        try:
            import pandas as pd
        except ImportError:
            raise ImportError("Install pandas to use to_dataframe().")

        return pd.DataFrame([
            {
                "episode_id": ep.episode_id,
                "model": ep.model,
                "context1": ep.context1,
                "context2": ep.context2
            }
            for ep in self._episodes
        ])
