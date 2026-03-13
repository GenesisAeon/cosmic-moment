# CLI Reference

The `cm` entrypoint provides two commands for observing and simulating cosmic moments.

---

## `cm detect`

Detect collapse points where `modulated_entropy(S_A, S_V)` exceeds the given threshold.

```
Usage: cm detect [OPTIONS]

Options:
  --threshold FLOAT   Collapse detection threshold [default: 0.618]
  --steps INTEGER     Number of time steps to evaluate [default: 100]
  --help              Show this message and exit.
```

**Examples**

```bash
# Default: golden-ratio threshold, 100 steps
cm detect

# Custom threshold
cm detect --threshold 0.5

# Higher resolution scan
cm detect --threshold 0.618 --steps 500
```

---

## `cm collapse`

Trigger a frame collapse at a given time coordinate and record the event.

```
Usage: cm collapse [OPTIONS]

Options:
  --t FLOAT   Time coordinate of the collapse [default: 3.14]
  --help      Show this message and exit.
```

**Examples**

```bash
# Default collapse at π
cm collapse

# Collapse at a specific moment
cm collapse --t 6.28
```

---

## Summary

| Command | Description |
|---------|-------------|
| `cm detect [--threshold FLOAT] [--steps INT]` | Detect collapse points where modulated duality exceeds threshold |
| `cm collapse [--t FLOAT]` | Trigger frame collapse at a cosmic moment |
