"""Tests for the cm CLI commands."""

from typer.testing import CliRunner

from cosmic_moment.cli import app

runner = CliRunner()


def test_detect_default():
    result = runner.invoke(app, ["detect"])
    assert result.exit_code == 0
    assert "cosmic moment" in result.output.lower()


def test_detect_custom_threshold():
    result = runner.invoke(app, ["detect", "--threshold", "0.5", "--steps", "50"])
    assert result.exit_code == 0
    assert "cosmic moment" in result.output.lower()


def test_detect_high_threshold_zero_moments():
    result = runner.invoke(app, ["detect", "--threshold", "999.0", "--steps", "20"])
    assert result.exit_code == 0
    assert "0 cosmic moment" in result.output.lower()


def test_collapse_default():
    result = runner.invoke(app, ["collapse"])
    assert result.exit_code == 0
    assert "collapsed" in result.output.lower()


def test_collapse_custom_t():
    result = runner.invoke(app, ["collapse", "--t", "6.28"])
    assert result.exit_code == 0
    assert "6.280" in result.output


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "detect" in result.output
    assert "collapse" in result.output
