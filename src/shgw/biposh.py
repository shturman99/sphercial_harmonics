"""Minimal symbolic scaffolding for BipoSH expressions."""

from __future__ import annotations

from sympy import Expr, Symbol


def biposh_symbol(label: str) -> Expr:
    """Return a placeholder symbol for a BipoSH coefficient."""
    return Symbol(label)
