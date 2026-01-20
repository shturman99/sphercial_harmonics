"""Tests for Clebsch--Gordan identities."""

from __future__ import annotations

import pytest
from sympy import Integer

from shgw.cg import cg_coeff, cg_to_3j
from shgw.texlink import Identity, is_zero, register_identity


@pytest.mark.parametrize(
    "values",
    [
        (1, 0, 1, 0, 0, 0),
        (1, 1, 1, -1, 1, 0),
        (2, 1, 1, 0, 1, 1),
        (2, 2, 1, -1, 1, 1),
    ],
)
def test_cg_to_3j_identity_values(values: tuple[int, int, int, int, int, int]) -> None:
    """Ensure the CG-to-3j relation holds for sample integers."""
    ell_1, m_1, ell_2, m_2, ell, m = values
    expr = cg_coeff(ell_1, m_1, ell_2, m_2, ell, m) - cg_to_3j(
        ell_1, m_1, ell_2, m_2, ell, m
    )
    assert is_zero(expr)


def test_registry_duplicate_label_rejected() -> None:
    """Ensure duplicate label registration is rejected."""
    from shgw import cg  # noqa: F401

    with pytest.raises(ValueError):
        register_identity("eq:cg:to3j", lambda: Identity("eq:cg:to3j", Integer(0)))
