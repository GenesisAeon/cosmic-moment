"""CosmicMoment — collapse detection and frame simulation."""

from __future__ import annotations

import numpy as np
from implosive_genesis.chronology import ChronologyValidator
from medium_modulation.core import modulated_entropy


def _baseline_threshold(S_A: float, S_V: float) -> float:
    """The unmodulated duality value (sin(freq*t)=0), used as the default
    collapse-detection threshold.

    For depth=0.5, freq=1.0 the achievable S_mod range is symmetric around
    this value, so it is the natural midpoint rather than an arbitrary
    constant -- unlike the previous hardcoded default of 0.618, which sat
    below the formula's achievable minimum (~0.927 for the default S_A/S_V),
    guaranteeing every t would be detected as a "moment" regardless of the
    actual modulation (see cosmic-moment-blindtest).
    """
    return modulated_entropy(S_A, S_V, depth=0.5, freq=1.0, t=0.0)


class CosmicMoment:
    """A single discrete cosmic moment of emergence."""

    def __init__(self) -> None:
        self.validator = ChronologyValidator()
        self.history: list[dict] = []

    def detect(
        self,
        S_A: float = 1.0,
        S_V: float = 1.618,
        threshold: float | None = None,
        steps: int = 100,
    ) -> list[float]:
        """Detect collapse points where modulated duality exceeds threshold.

        Args:
            S_A: Entropic amplitude (S∝A side of duality).
            S_V: Entropic volume (S∝V side of duality).
            threshold: Collapse detection threshold. Defaults to the
                unmodulated duality baseline for the given S_A/S_V (see
                :func:`_baseline_threshold`), which makes detection
                genuinely selective instead of matching every t.
            steps: Number of time steps to evaluate.

        Returns:
            List of time points where a cosmic moment was detected.
        """
        if threshold is None:
            threshold = _baseline_threshold(S_A, S_V)
        t = np.linspace(0, 10, steps)
        moments: list[float] = []
        for ti in t:
            S_mod = modulated_entropy(S_A, S_V, depth=0.5, freq=1.0, t=float(ti))
            if S_mod > threshold:
                moments.append(round(float(ti), 3))
        # implosive-genesis 10-part chronology check
        chronology = self.validator.validate()
        if not chronology.passed:
            raise RuntimeError(
                f"implosive-genesis chronology validation failed "
                f"({chronology.n_passed}/{chronology.n_total} parts passed): "
                f"{chronology.summary}"
            )
        return moments

    def collapse(self, t: float, S_A: float = 1.0, S_V: float = 1.618) -> dict:
        """Simulate frame collapse at a cosmic moment.

        Args:
            t: Time coordinate of the collapse.
            S_A: Entropic amplitude, same meaning as in :meth:`detect`.
            S_V: Entropic volume, same meaning as in :meth:`detect`.

        Returns:
            Collapse event record. ``collapsed`` and ``new_layer`` now
            genuinely depend on the modulated duality at *t* (previously
            both were hardcoded constants regardless of *t*; see
            cosmic-moment-blindtest).
        """
        S_mod = modulated_entropy(S_A, S_V, depth=0.5, freq=1.0, t=t)
        collapsed = bool(S_mod > _baseline_threshold(S_A, S_V))
        moment: dict = {
            "timestamp": t,
            "collapsed": collapsed,
            "new_layer": "consciousness" if collapsed else "dormant",
            "S_mod": round(float(S_mod), 6),
        }
        self.history.append(moment)
        return moment
