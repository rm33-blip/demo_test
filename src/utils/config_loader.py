import os
import yaml


def load_config(path: str) -> dict:
    """
    Load YAML config from disk.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
