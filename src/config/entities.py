from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeContext:
    """
    Small immutable entity representing runtime config/context.
    """
    env: str
    mode: str
