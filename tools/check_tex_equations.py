"""Check that required LaTeX equation labels have Python identities."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from shgw import cg  # noqa: F401
from shgw.texlink import registered_labels

LABEL_PATTERN = re.compile(r"\\label\{(eq:[^}]+)\}")
REQUIRED_LABELS = {"eq:cg:to3j"}


def extract_labels(tex_text: str) -> set[str]:
    """Extract equation labels from TeX content."""
    return set(LABEL_PATTERN.findall(tex_text))


def check_required_labels(tex_path: Path, required: set[str]) -> int:
    """Return nonzero when required labels are missing."""
    tex_labels = extract_labels(tex_path.read_text(encoding="utf-8"))
    missing_in_tex = required - tex_labels
    missing_in_registry = required - registered_labels()

    if missing_in_tex:
        print(
            "Required labels missing from TeX: " + ", ".join(sorted(missing_in_tex)),
            file=sys.stderr,
        )
    if missing_in_registry:
        print(
            "Required labels missing from registry: "
            + ", ".join(sorted(missing_in_registry)),
            file=sys.stderr,
        )

    return 1 if missing_in_tex or missing_in_registry else 0


def main() -> int:
    """CLI entry point."""
    tex_path = Path("scartch.tex")
    return check_required_labels(tex_path, REQUIRED_LABELS)


if __name__ == "__main__":
    raise SystemExit(main())
