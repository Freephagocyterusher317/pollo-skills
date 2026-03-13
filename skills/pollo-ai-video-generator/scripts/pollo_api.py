#!/usr/bin/env python3
"""
Unified API wrapper for Pollo AI. Keeps API key out of LLM context.

Usage:
    python3 pollo_api.py <METHOD> <endpoint> [--data JSON] [--upload FILE]

Examples:
    python3 pollo_api.py GET /credit/balance
    python3 pollo_api.py POST /generation/pollo/pollo-v2-0 --data '{"input":{...}}'
    python3 pollo_api.py POST /file/sign --data '{"action":"putObject","filename":"photo.jpg","type":"image/jpeg"}'
    python3 pollo_api.py PUT <signed-url> --upload /path/to/file.jpg --content-type image/jpeg

Exit codes: 0 = success, 1 = API error, 2 = config error
"""

import argparse
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional, Tuple, Union

# Import config from same directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pollo_config import load_config


def api_request(method: str, url: str, headers: dict, data: Optional[bytes] = None) -> Tuple[int, Union[dict, str]]:
    """Make HTTP request, return (status_code, parsed_response)."""
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = resp.read().decode()
            try:
                return resp.status, json.loads(body)
            except json.JSONDecodeError:
                return resp.status, body
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode()
        except Exception:
            pass
        try:
            return e.code, json.loads(body)
        except json.JSONDecodeError:
            return e.code, {"error": body, "status_code": e.code}


def main():
    parser = argparse.ArgumentParser(description="Pollo AI API wrapper")
    parser.add_argument("method", choices=["GET", "POST", "PUT"], help="HTTP method")
    parser.add_argument("endpoint", help="API endpoint (e.g. /credit/balance) or full URL for PUT uploads")
    parser.add_argument("--data", help="JSON request body")
    parser.add_argument("--upload", help="File path to upload (binary PUT)")
    parser.add_argument("--content-type", default="application/octet-stream", help="Content-Type for file upload")

    args = parser.parse_args()

    # For PUT uploads to signed URLs (external), skip config loading
    is_external_url = args.endpoint.startswith("http://") or args.endpoint.startswith("https://")

    if is_external_url and args.upload:
        # Direct file upload to signed URL — no API key needed
        file_path = Path(args.upload)
        if not file_path.exists():
            print(json.dumps({"error": f"File not found: {args.upload}"}))
            sys.exit(1)

        file_data = file_path.read_bytes()
        headers = {"Content-Type": args.content_type}
        status, response = api_request(args.method, args.endpoint, headers, file_data)
    else:
        # Normal API call — load config for key
        try:
            config = load_config()
        except (FileNotFoundError, ValueError) as e:
            print(json.dumps({"error": str(e)}))
            sys.exit(2)

        url = config["base_url"].rstrip("/") + args.endpoint if not is_external_url else args.endpoint

        headers = {
            "X-API-KEY": config["api_key"],
            "Content-Type": "application/json",
            "User-Agent": "Pollo-AI-Skill/1.0",
        }

        body = args.data.encode() if args.data else None
        status, response = api_request(args.method, url, headers, body)

    # Output result
    if isinstance(response, dict):
        print(json.dumps(response, indent=2, ensure_ascii=False))
    else:
        print(response)

    # Exit code based on HTTP status
    if 200 <= status < 300:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
