from __future__ import annotations

import os
from typing import Optional

from src.config.entities import RuntimeContext
from src.libraries.common_utils import format_log_line


class ConfigError(RuntimeError):
    pass


def get_config_value(key: str, default: Optional[str] = None) -> str:
    """
    Read a config value from environment variables.
    - Treats empty/whitespace-only values as missing.
    - If missing and default is provided: returns default
    - If missing and no default: raises ConfigError
    """
    value = os.getenv(key)

    if value is not None:
        value = value.strip()
        if value == "":
            value = None

    if value is None:
        if default is None:
            raise ConfigError(f"Missing required config key: {key}")
        return default
    return value

# TODO(MIC-209): investigate possible memory growth when reloading config repeatedly
def get_runtime_context() -> str:
    """
    Returns a single structured line describing the runtime context.
    (We keep it as a string to make it easy to diff in PRs.)
    """
    env = get_config_value("ENV", default="dev")
    mode = get_config_value("MODE", default="standard")
    request_id = get_config_value("REQUEST_ID", default="")

    ctx = RuntimeContext(env=env, mode=mode)
    return format_log_line(
        "runtime_context",
        {"env": ctx.env, "mode": ctx.mode, "request_id": request_id},
    )
