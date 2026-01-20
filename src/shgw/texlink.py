"""Registry linking LaTeX equation labels to symbolic identities."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict

from sympy import Expr, simplify


@dataclass(frozen=True)
class Identity:
    """Symbolic identity keyed by a LaTeX equation label."""

    label: str
    expression: Expr
    description: str | None = None


IdentityFactory = Callable[[], Identity]

_REGISTRY: Dict[str, IdentityFactory] = {}


def register_identity(label: str, factory: IdentityFactory) -> None:
    """Register an identity factory under a LaTeX equation label."""
    if label in _REGISTRY:
        raise ValueError(f"Identity label already registered: {label}")
    _REGISTRY[label] = factory


def get_identity(label: str) -> Identity:
    """Construct the identity for a given label."""
    return _REGISTRY[label]()


def registered_labels() -> set[str]:
    """Return the set of registered LaTeX equation labels."""
    return set(_REGISTRY.keys())


def is_zero(expr: Expr) -> bool:
    """Return True when the expression simplifies to zero."""
    return simplify(expr) == 0


def check_identity(identity: Identity) -> bool:
    """Return True when the identity expression simplifies to zero."""
    return is_zero(identity.expression)
