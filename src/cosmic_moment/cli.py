"""Typer CLI for cosmic-moment — `cm` entrypoint."""

from __future__ import annotations

import typer
from rich.console import Console

from .core import CosmicMoment

app = typer.Typer(help="Cosmic Moment CLI – discrete points of cosmic self-awareness.")
console = Console()

_cm = CosmicMoment()


@app.command()
def detect(
    threshold: float = typer.Option(0.618, help="Collapse detection threshold."),
    steps: int = typer.Option(100, help="Number of time steps to evaluate."),
) -> None:
    """Detect cosmic moments of emergence."""
    moments = _cm.detect(threshold=threshold, steps=steps)
    console.print(f"[bold magenta]Detected {len(moments)} cosmic moment(s)[/]")
    if moments:
        console.print(f"First at t = {moments[0]}")


@app.command()
def collapse(
    t: float = typer.Option(3.14, help="Time coordinate of the collapse."),
) -> None:
    """Trigger frame collapse at a cosmic moment."""
    result = _cm.collapse(t)
    console.print(
        f"[bold cyan]Frame collapsed at t={result['timestamp']:.3f} "
        f"→ new {result['new_layer']} layer[/]"
    )


if __name__ == "__main__":
    app()
