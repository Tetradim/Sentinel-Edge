"""Runtime mode helpers shared by Edge API and scheduler."""

from __future__ import annotations

def env_flag_enabled(name: str, default: str = "false") -> bool:
    import os

    return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "on"}


def is_dry_run_enabled() -> bool:
    """Dry-run handoff suppression has been removed from live broker testing."""
    return False
