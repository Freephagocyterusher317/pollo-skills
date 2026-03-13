#!/usr/bin/env python3
"""
Interactive setup for Pollo AI API key.

Usage:
    python3 pollo_setup.py              # interactive prompt
    python3 pollo_setup.py --key <key>  # non-interactive

Creates ~/.pollo/config.toml with validated API credentials.
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pollo_config import CONFIG_PATH, DEFAULT_BASE_URL


def validate_key(api_key: str, base_url: str = DEFAULT_BASE_URL) -> Optional[dict]:
    """Validate API key by checking credit balance. Returns balance dict or None."""
    url = f"{base_url.rstrip('/')}/credit/balance"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
        "User-Agent": "Pollo-AI-Skill/1.0",
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode()
        except Exception:
            pass
        try:
            error = json.loads(body)
        except json.JSONDecodeError:
            error = {"error": body}
        code = error.get("code", "")
        if code == "NOT_FOUND" or e.code == 404:
            print("Error: API key is invalid or does not exist.")
            print("Please check your key at https://pollo.ai/api-platform/keys")
        elif code == "UNAUTHORIZED" or e.code == 401:
            print("Error: API key format is incorrect. Keys start with 'pollo_'.")
            print("Get yours at https://pollo.ai/api-platform/keys")
        else:
            print(f"Error: API returned HTTP {e.code}: {body}")
        return None
    except (urllib.error.URLError, OSError, TimeoutError) as e:
        print(f"Error: Could not reach API — {e}")
        print("Please check your network and try again.")
        return None


def write_config(api_key: str, base_url: str = DEFAULT_BASE_URL):
    """Write config.toml to ~/.pollo/."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    content = f"""# Pollo AI Configuration
# Docs: https://pollo.ai/api-platform

[api]
key = "{api_key}"
base_url = "{base_url}"
"""
    CONFIG_PATH.write_text(content, encoding="utf-8")
    CONFIG_PATH.chmod(0o600)  # Only owner can read


def main():
    parser = argparse.ArgumentParser(description="Set up Pollo AI API key")
    parser.add_argument("--key", help="API key (non-interactive mode)")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL, help="Base URL override")
    args = parser.parse_args()

    print("=== Pollo AI Setup ===\n")

    # Check existing config
    if CONFIG_PATH.exists():
        print(f"Existing config found at {CONFIG_PATH}")
        try:
            from pollo_config import load_config
            existing = load_config()
            masked = existing["api_key"][:8] + "..." + existing["api_key"][-4:]
            print(f"  Current key: {masked}")
        except Exception:
            print("  (could not read existing config)")

        if not args.key:
            answer = input("\nUpdate config? [y/N] ").strip().lower()
            if answer != "y":
                print("Keeping existing config.")
                return

    # Get API key
    if args.key:
        api_key = args.key.strip()
    else:
        print("Get your API key at: https://pollo.ai/api-platform/keys\n")
        api_key = input("Enter your API key: ").strip()

    if not api_key:
        print("Error: No API key provided.")
        sys.exit(1)

    # Validate
    print("\nValidating key...")
    balance = validate_key(api_key, args.base_url)
    if balance is None:
        sys.exit(1)

    # Write config
    write_config(api_key, args.base_url)

    # API wraps successful responses in { "code", "message", "data": { ... } }
    inner = balance.get("data", balance)
    available = inner.get("availableCredits", 0)
    total = inner.get("totalCredits", 0)

    print(f"\nSetup complete!")
    print(f"  Config: {CONFIG_PATH}")
    print(f"  Credits: {available} / {total}")

    if available == 0:
        print("\n  Warning: Your balance is 0 credits.")
        print("  Top up at https://pollo.ai/api-platform/pricing")


if __name__ == "__main__":
    main()
