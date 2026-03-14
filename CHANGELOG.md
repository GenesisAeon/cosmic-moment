# Changelog

All notable changes to `cosmic-moment` are documented here.

---

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
