"""Clebsch--Gordan and Wigner 3j relations."""

from __future__ import annotations

from sympy import Expr, sqrt
from sympy.physics.wigner import clebsch_gordan, wigner_3j

from .symbols import L, M, l1, l2, m1, m2
from .texlink import Identity, register_identity


def cg_coeff(
    ell_1: Expr, m_1: Expr, ell_2: Expr, m_2: Expr, ell: Expr, m: Expr
) -> Expr:
    """Return the Clebsch--Gordan coefficient <l1 m1 l2 m2 | L M>."""
    return clebsch_gordan(ell_1, ell_2, ell, m_1, m_2, m)


def cg_to_3j(
    ell_1: Expr, m_1: Expr, ell_2: Expr, m_2: Expr, ell: Expr, m: Expr
) -> Expr:
    """Convert Clebsch--Gordan coefficients to Wigner 3j symbols."""
    return (-1) ** (ell_1 - ell_2 + m) * sqrt(2 * ell + 1) * wigner_3j(
        ell_1, ell_2, ell, m_1, m_2, -m
    )


def identity_cg_to_3j() -> Identity:
    """Identity linking CG coefficients and Wigner 3j symbols."""
    expression = cg_coeff(l1, m1, l2, m2, L, M) - cg_to_3j(l1, m1, l2, m2, L, M)
    return Identity(label="eq:cg:to3j", expression=expression)


register_identity("eq:cg:to3j", identity_cg_to_3j)
