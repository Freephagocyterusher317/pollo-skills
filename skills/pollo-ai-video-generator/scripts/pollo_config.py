#!/usr/bin/env python3
"""
Shared config module for Pollo AI scripts.

Reads API key and base URL from ~/.pollo/config.toml.
Uses a minimal TOML parser — no external dependencies.
"""

import re
import sys
from pathlib import Path

CONFIG_PATH = Path.home() / ".pollo" / "config.toml"

DEFAULT_BASE_URL = "https://pollo.ai/api/platform"


def parse_toml_simple(text: str) -> dict:
    """Minimal TOML parser supporting [section] and key = "value" pairs."""
    result = {}
    current_section = None

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        section_match = re.match(r"^\[([a-zA-Z0-9_.-]+)\]$", line)
        if section_match:
            current_section = section_match.group(1)
            result.setdefault(current_section, {})
            continue

        kv_match = re.match(r'^([a-zA-Z0-9_-]+)\s*=\s*"((?:[^"\\]|\\.)*)"$', line)
        if not kv_match:
            kv_match = re.match(r"^([a-zA-Z0-9_-]+)\s*=\s*'((?:[^'\\]|\\.)*)'$", line)
        if kv_match:
            key, value = kv_match.group(1), kv_match.group(2)
            value = value.replace('\\"', '"').replace("\\'", "'")
            if current_section:
                result[current_section][key] = value
            else:
                result[key] = value

    return result


def load_config() -> dict:
    """Load config from ~/.pollo/config.toml. Returns dict with api_key and base_url."""
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Config not found at {CONFIG_PATH}\n"
            f"Run: python3 scripts/pollo_setup.py"
        )

    text = CONFIG_PATH.read_text(encoding="utf-8")
    parsed = parse_toml_simple(text)

    api_section = parsed.get("api", {})
    api_key = api_section.get("key", "")
    base_url = api_section.get("base_url", DEFAULT_BASE_URL)

    if not api_key:
        raise ValueError(
            f"No API key found in {CONFIG_PATH}\n"
            f"Run: python3 scripts/pollo_setup.py"
        )

    return {"api_key": api_key, "base_url": base_url}


def get_api_key() -> str:
    """Convenience: return just the API key string."""
    return load_config()["api_key"]


if __name__ == "__main__":
    try:
        config = load_config()
        print(f"Config loaded from {CONFIG_PATH}")
        print(f"  base_url: {config['base_url']}")
        print(f"  api_key:  {config['api_key'][:8]}...{config['api_key'][-4:]}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)
