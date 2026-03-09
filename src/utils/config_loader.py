import os
import yaml

# Simple in-process cache: {(path, mtime): parsed_config}
_CONFIG_CACHE = {}


def load_config(path: str) -> dict:
    """
    Load YAML config from disk with a small cache to reduce repeated parsing.

    Cache key uses file mtime so edits invalidate cache automatically.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    mtime = os.path.getmtime(path)
    cache_key = (path, mtime)

    if cache_key in _CONFIG_CACHE:
        return _CONFIG_CACHE[cache_key]

    with open(path, "r", encoding="utf-8") as f:
        parsed = yaml.safe_load(f) or {}

    _CONFIG_CACHE.clear()  # keep cache small (1-entry behavior)
    _CONFIG_CACHE[cache_key] = parsed
    return parsed
