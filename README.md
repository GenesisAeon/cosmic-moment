# cosmic-moment

**Discrete moments of cosmic emergence** — the fractal singularities where modulated entropy duality collapses into conscious presence.

[![CI](https://github.com/GenesisAeon/cosmic-moment/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/cosmic-moment/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/cosmic-moment)](https://pypi.org/project/cosmic-moment/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Built directly on **medium-modulation**, **entropy-governance** and **implosive-genesis** chronology.

---

## Install

```bash
pip install cosmic-moment
```

**DOI**: [10.5281/zenodo.19010800](https://doi.org/10.5281/zenodo.19010800)   **PyPI**: `pip install cosmic-moment==0.1.0`  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19010800.svg)](https://doi.org/10.5281/zenodo.19010800)

## Usage

```bash
cm detect --threshold 0.618
cm collapse --t 3.14
```

## Quick start (Python)

```python
from cosmic_moment.core import CosmicMoment

cm = CosmicMoment()
moments = cm.detect(threshold=0.618, steps=100)
print(f"Detected {len(moments)} cosmic moments")

frame = cm.collapse(moments[0])
print(frame)
```

## CLI Reference

| Command | Description |
|---------|-------------|
| `cm detect [--threshold FLOAT] [--steps INT]` | Detect collapse points where modulated duality exceeds threshold |
| `cm collapse [--t FLOAT]` | Trigger frame collapse at a cosmic moment |

## Stack integration

| Package | Role |
|---------|------|
| `medium-modulation` | `modulated_entropy` — core S∝A ↔ S∝V duality signal |
| `implosive-genesis` | `ChronologyValidator` — 10-part chronology check |
| `entropy-governance` | governance constraints on entropy flow |
| `entropy-table` | `EntropyTable` — domain relation persistence |

## Project structure

```
cosmic-moment/
├── pyproject.toml
├── README.md
├── domains.yaml
├── src/
│   └── cosmic_moment/
│       ├── __init__.py
│       ├── core.py                  # CosmicMoment + collapse detection
│       ├── cli.py                   # Typer CLI (cm)
│       └── entropy_table_bridge.py  # EntropyTable integration
├── tests/
│   ├── test_core.py
│   └── test_cli.py
└── mkdocs.yml
```

---


Built with [uv](https://docs.astral.sh/uv/) · [Typer](https://typer.tiangolo.com/) · [Rich](https://rich.readthedocs.io/) · [SymPy](https://www.sympy.org/)
