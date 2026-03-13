"""Bridge between cosmic-moment and entropy-table for domain relation persistence."""

from __future__ import annotations

from pathlib import Path

from entropy_table import EntropyTable


class CosmicMomentBridge:
    """Persist cosmic-moment domain relations via entropy-table."""

    def __init__(self) -> None:
        self.table = EntropyTable(domain="cosmic-moment")

    def add_moment(self, key: str, value: float) -> None:
        """Register a cosmic moment relation in the entropy table."""
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path | str:
        """Export all domain relations to a YAML file."""
        self.table.export(filepath)
        return filepath
