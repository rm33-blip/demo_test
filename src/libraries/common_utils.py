from __future__ import annotations

import json
from typing import Any, Dict


def format_log_line(message: str, fields: Dict[str, Any] | None = None) -> str:
    """
    Minimal JSON-line formatter to simulate structured logs.
    """
    payload: Dict[str, Any] = {"message": message}
    if fields:
        payload.update(fields)
    return json.dumps(payload, ensure_ascii=False)


def safe_lower(s: str | None) -> str | None:
    """
    Small helper used in some PRs to show safe handling of null-ish strings.
    """
    return s.lower() if s is not None else None
