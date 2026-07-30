"""Bridge between cosmic-moment and entropy-table for domain relation persistence."""

from __future__ import annotations

from pathlib import Path


class CosmicMomentBridge:
    """Persist cosmic-moment domain relations via entropy-table.

    Requires the ``entropy-table`` optional dependency to be installed.
    Import is deferred so the package is usable without it.

    Raises:
        ImportError: if ``entropy-table`` is not installed at all.
        RuntimeError: if ``entropy-table`` is installed but its API no
            longer matches what this bridge expects (see below).
    """

    def __init__(self) -> None:
        from importlib.metadata import PackageNotFoundError
        from importlib.metadata import version as _version

        try:
            _installed_version: str | None = _version("entropy-table")
        except PackageNotFoundError:
            _installed_version = None

        try:
            from entropy_table import EntropyTable  # type: ignore
        except ImportError as exc:
            if _installed_version is None:
                raise ImportError(
                    "entropy-table is required for CosmicMomentBridge. "
                    "Install it with: pip install entropy-table"
                ) from exc
            # entropy-table >=2.0 removed the EntropyTable class entirely
            # in favor of a different "contract-first" case/claim-ID data
            # model. This bridge was written against the pre-2.0 API and
            # was never updated. Previously this was a bare top-level
            # import, so it crashed the whole module on import with no
            # error handling at all rather than raising even a wrong
            # error message. Found via an ecosystem-wide sweep of sibling
            # bridge files after the same bug was confirmed in
            # climate-dashboard.
            raise RuntimeError(
                f"entropy-table {_installed_version} is installed, but its API no "
                "longer matches what this bridge expects (no EntropyTable class "
                "-- entropy-table >=2.0 replaced the domain-relation model "
                "entirely). This bridge needs updating for the current "
                "entropy-table API; it is not simply a missing dependency."
            ) from exc

        self.table = EntropyTable(domain="cosmic-moment")

    def add_moment(self, key: str, value: float) -> None:
        """Register a cosmic moment relation in the entropy table."""
        self.table.add_relation(key, value)

    def export(self, filepath: Path | str = "domains.yaml") -> Path | str:
        """Export all domain relations to a YAML file."""
        self.table.export(filepath)
        return filepath
