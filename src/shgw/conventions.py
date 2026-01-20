"""Phase and parity conventions aligned with the LaTeX notes."""

from __future__ import annotations

def condon_shortley_phase(m: int) -> int:
    """Return the Condon--Shortley phase (-1)^m."""
    return int((-1) ** int(m))


def parity_sign(ell: int) -> int:
    """Return the parity factor (-1)^ell."""
    return int((-1) ** int(ell))
