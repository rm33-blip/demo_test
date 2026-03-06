import os
import yaml

_CACHE = {}


def load_config(path: str) -> dict:
    """
    Load YAML config from disk.
    Cache by (path, mtime) to avoid reparsing unchanged configs.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")

    mtime = os.path.getmtime(path)
    cache_key = (path, mtime)

    if cache_key in _CACHE:
        return _CACHE[cache_key]

    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    _CACHE[cache_key] = cfg
    return cfg
