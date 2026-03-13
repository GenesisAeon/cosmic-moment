"""Tests for CosmicMoment core logic."""

from cosmic_moment.core import CosmicMoment


def test_detect_returns_list():
    cm = CosmicMoment()
    moments = cm.detect(steps=50)
    assert isinstance(moments, list)


def test_detect_returns_moments():
    cm = CosmicMoment()
    moments = cm.detect(steps=50)
    assert len(moments) > 0
    assert isinstance(moments[0], float)


def test_detect_threshold_filters():
    cm = CosmicMoment()
    # Very high threshold — should return fewer moments
    moments_high = cm.detect(threshold=10.0, steps=50)
    moments_low = cm.detect(threshold=0.1, steps=50)
    assert len(moments_high) <= len(moments_low)


def test_detect_steps_affect_resolution():
    cm = CosmicMoment()
    moments_coarse = cm.detect(steps=10)
    moments_fine = cm.detect(steps=200)
    # More steps → at least as many moments
    assert len(moments_fine) >= len(moments_coarse)


def test_collapse_returns_dict():
    cm = CosmicMoment()
    result = cm.collapse(3.14)
    assert isinstance(result, dict)
    assert result["collapsed"] is True
    assert result["timestamp"] == 3.14
    assert result["new_layer"] == "consciousness"


def test_collapse_appends_to_history():
    cm = CosmicMoment()
    cm.collapse(1.0)
    cm.collapse(2.0)
    assert len(cm.history) == 2
    assert cm.history[0]["timestamp"] == 1.0
    assert cm.history[1]["timestamp"] == 2.0


def test_history_starts_empty():
    cm = CosmicMoment()
    assert cm.history == []
