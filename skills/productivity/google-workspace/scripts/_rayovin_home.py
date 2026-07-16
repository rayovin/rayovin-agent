"""Resolve RAYOVIN_HOME for standalone skill scripts.

Skill scripts may run outside the Rayovin process (e.g. system Python,
nix env, CI) where ``rayovin_constants`` is not importable.  This module
provides the same ``get_rayovin_home()`` and ``display_rayovin_home()``
contracts as ``rayovin_constants`` without requiring it on ``sys.path``.

When ``rayovin_constants`` IS available it is used directly so that any
future enhancements (profile resolution, Docker detection, etc.) are
picked up automatically.  The fallback path replicates the core logic
from ``rayovin_constants.py`` using only the stdlib.

All scripts under ``google-workspace/scripts/`` should import from here
instead of duplicating the ``RAYOVIN_HOME = Path(os.getenv(...))`` pattern.
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    from rayovin_constants import display_rayovin_home as display_rayovin_home
    from rayovin_constants import get_rayovin_home as get_rayovin_home
except (ModuleNotFoundError, ImportError):

    def get_rayovin_home() -> Path:
        """Return the Rayovin home directory (default: ~/.rayovin).

        Mirrors ``rayovin_constants.get_rayovin_home()``."""
        val = os.environ.get("RAYOVIN_HOME", "").strip()
        return Path(val) if val else Path.home() / ".rayovin"

    def display_rayovin_home() -> str:
        """Return a user-friendly ``~/``-shortened display string.

        Mirrors ``rayovin_constants.display_rayovin_home()``."""
        home = get_rayovin_home()
        try:
            return "~/" + str(home.relative_to(Path.home()))
        except ValueError:
            return str(home)
