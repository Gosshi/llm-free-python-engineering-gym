"""Check the local prerequisites without modifying the challenge."""

from __future__ import annotations

import sys


def main() -> int:
    if sys.version_info[:2] != (3, 13):
        print(f"Python 3.13 is required; running {sys.version.split()[0]}.")
        return 1

    try:
        import fastapi  # noqa: F401
        import pydantic  # noqa: F401
        import pytest  # noqa: F401
        import ruff  # noqa: F401
    except ImportError as error:
        print(f"A required package is missing: {error.name}")
        return 1

    print(f"Python {sys.version.split()[0]} and required packages are available.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
