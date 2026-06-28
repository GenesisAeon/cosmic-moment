# Changelog

All notable changes to `cosmic-moment` are documented here.

---

## [1.0.0] – 2026-06-28

### Added

- Standardized ecosystem release tooling: `.zenodo.json`, `RELEASE_GUIDE.md`,
  `CONTRIBUTING.md`, issue/PR templates.

### Changed

- Project metadata (`pyproject.toml`) normalized for the GenesisAeon
  ecosystem v1.0.0 milestone: version bumped to `1.0.0`, dependency pins
  raised to `medium-modulation>=1.0.0`, `entropy-governance>=1.0.0`,
  `entropy-table>=2.0.0`, `implosive-genesis>=1.0.0`.
- **Relicensed** from MIT to dual-license: source code under
  GPL-3.0-or-later (`LICENSE-CODE`), documentation under CC BY 4.0
  (`LICENSE-DOCS`).
- Fixed CI: added `mypy` to the `dev` extra, installed the `docs` extra
  in the docs job, and dropped Python 3.10 from the test matrix (the
  package requires Python >=3.11).

## [0.1.0] – 2026-03-13

**First Cosmic Moments of Emergence**

### Added

- `CosmicMoment.detect(S_A, S_V, threshold, steps)` — discrete detection of collapse points where `modulated_entropy(S_A, S_V)` exceeds threshold
- `CosmicMoment.collapse(t)` — simulate frame collapse at a given time coordinate, returning a structured event record
- CLI entrypoint `cm` with two commands:
  - `cm detect [--threshold FLOAT] [--steps INT]`
  - `cm collapse [--t FLOAT]`
- `CosmicMomentBridge` — persist domain relations via `entropy-table` (`domains.yaml`)
- Full integration with the GenesisAeon stack:
  - `medium-modulation` — `modulated_entropy` S∝A ↔ S∝V duality signal
  - `implosive-genesis` — `ChronologyValidator` 10-part chronology check
  - `entropy-governance` — governance constraints on entropy flow
  - `entropy-table` — domain relation persistence
- 99 % test coverage (pytest-cov), ruff clean, mkdocs --strict clean
- MIT License
