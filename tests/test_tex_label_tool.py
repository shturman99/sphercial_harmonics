"""Tests for TeX label extraction and registry coverage."""

from __future__ import annotations

from pathlib import Path

from shgw import cg  # noqa: F401
from shgw.texlink import registered_labels
from tools.check_tex_equations import REQUIRED_LABELS, extract_labels


def test_required_labels_registered() -> None:
    """Ensure required TeX labels are registered in Python."""
    tex_labels = extract_labels(Path("scartch.tex").read_text(encoding="utf-8"))
    missing_in_tex = REQUIRED_LABELS - tex_labels
    missing_in_registry = REQUIRED_LABELS - registered_labels()

    assert not missing_in_tex
    assert not missing_in_registry
