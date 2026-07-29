"""Typer CLI for cosmic-moment — `cm` entrypoint."""

from __future__ import annotations

import io
import sys

import typer
from rich.console import Console

from .core import CosmicMoment

# Windows consoles default to a non-UTF-8 codepage, which breaks the arrow
# and other math symbols used in this CLI's output with UnicodeEncodeError.
# Force UTF-8 stdout/stderr so behavior matches Linux/macOS terminals.
if isinstance(sys.stdout, io.TextIOWrapper):
    sys.stdout.reconfigure(encoding="utf-8")
if isinstance(sys.stderr, io.TextIOWrapper):
    sys.stderr.reconfigure(encoding="utf-8")

app = typer.Typer(help="Cosmic Moment CLI – discrete points of cosmic self-awareness.")
console = Console()

_cm = CosmicMoment()


@app.command()
def detect(
    threshold: float | None = typer.Option(
        None,
        help="Collapse detection threshold. Defaults to the unmodulated "
        "duality baseline for the given S_A/S_V.",
    ),
    steps: int = typer.Option(100, help="Number of time steps to evaluate."),
) -> None:
    """Detect cosmic moments of emergence."""
    moments = _cm.detect(threshold=threshold, steps=steps)
    console.print(
        f"[bold magenta]Detected {len(moments)} cosmic moment(s)[/]", highlight=False
    )
    if moments:
        console.print(f"First at t = {moments[0]}", highlight=False)


@app.command()
def collapse(
    t: float = typer.Option(3.14, help="Time coordinate of the collapse."),
) -> None:
    """Trigger frame collapse at a cosmic moment."""
    result = _cm.collapse(t)
    if result["collapsed"]:
        console.print(
            f"[bold cyan]Frame collapsed at t={result['timestamp']:.3f} "
            f"→ new {result['new_layer']} layer[/] (S_mod={result['S_mod']:.4f})",
            highlight=False,
        )
    else:
        console.print(
            f"[bold yellow]No collapse at t={result['timestamp']:.3f}[/] "
            f"(S_mod={result['S_mod']:.4f} below baseline, "
            f"layer stays {result['new_layer']})",
            highlight=False,
        )


if __name__ == "__main__":
    app()
