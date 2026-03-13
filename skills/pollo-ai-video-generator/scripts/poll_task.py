#!/usr/bin/env python3
"""
Poll a Pollo AI generation task until completion.

Usage:
    python poll_task.py <task_id> [--api-key KEY] [--interval 5] [--timeout 300]

API key is read from ~/.pollo/config.toml by default.
Override with --api-key if needed.

Final JSON result is printed to stdout.
Exit codes: 0 = succeed, 1 = failed, 2 = timeout, 3 = error
"""

import argparse
import json
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# Import config from same directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pollo_config import load_config

def poll_task(task_id: str, api_key: str, base_url: str = "https://pollo.ai/api/platform", interval: int = 5, timeout: int = 300, max_retries: int = 5) -> dict:
    TRANSIENT_HTTP_CODES = {429, 500, 502, 503, 504}

    url = f"{base_url.rstrip('/')}/generation/{task_id}/status"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
        "User-Agent": "Pollo-AI-Skill/1.0",
    }

    start = time.time()
    attempt = 0
    consecutive_errors = 0

    while True:
        elapsed = time.time() - start
        if elapsed > timeout:
            return {"status": "timeout", "elapsed": round(elapsed, 1), "taskId": task_id}

        attempt += 1
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = json.loads(resp.read().decode())

            consecutive_errors = 0

            # API wraps result in { code, message, data: { ... } }
            data = raw.get("data", raw)
            generations = data.get("generations", [])
            if not generations:
                status = data.get("status", "processing")
            else:
                statuses = [g.get("status", "processing") for g in generations]
                if all(s == "succeed" for s in statuses):
                    status = "succeed"
                elif any(s == "failed" for s in statuses):
                    status = "failed"
                else:
                    status = "processing"

            if status == "succeed":
                urls = [g.get("url", "") for g in generations if g.get("url")]
                return {
                    "status": "succeed",
                    "taskId": task_id,
                    "urls": urls,
                    "elapsed": round(time.time() - start, 1),
                    "attempts": attempt,
                    "generations": generations,
                }
            elif status == "failed":
                fail_msgs = [g.get("failMsg", "") for g in generations if g.get("failMsg")]
                return {
                    "status": "failed",
                    "taskId": task_id,
                    "failMsg": "; ".join(fail_msgs) if fail_msgs else "Unknown error",
                    "elapsed": round(time.time() - start, 1),
                    "attempts": attempt,
                }

            time.sleep(interval)

        except urllib.error.HTTPError as e:
            error_body = ""
            try:
                error_body = e.read().decode()
            except Exception:
                pass

            if e.code in TRANSIENT_HTTP_CODES:
                consecutive_errors += 1
                if consecutive_errors >= max_retries:
                    return {
                        "status": "error",
                        "taskId": task_id,
                        "error": f"HTTP {e.code}: {error_body} (after {consecutive_errors} consecutive failures)",
                        "elapsed": round(time.time() - start, 1),
                    }
                backoff = min(interval * (2 ** consecutive_errors), 30)
                time.sleep(backoff)
            else:
                return {
                    "status": "error",
                    "taskId": task_id,
                    "error": f"HTTP {e.code}: {error_body}",
                    "elapsed": round(time.time() - start, 1),
                }
        except (urllib.error.URLError, OSError, TimeoutError) as e:
            consecutive_errors += 1
            if consecutive_errors >= max_retries:
                return {
                    "status": "error",
                    "taskId": task_id,
                    "error": f"{e} (after {consecutive_errors} consecutive failures)",
                    "elapsed": round(time.time() - start, 1),
                }
            backoff = min(interval * (2 ** consecutive_errors), 30)
            time.sleep(backoff)


def main():
    parser = argparse.ArgumentParser(description="Poll Pollo AI task status")
    parser.add_argument("task_id", help="The task ID to poll")
    parser.add_argument("--api-key", help="Pollo AI API key (reads from ~/.pollo/config.toml if omitted)")
    parser.add_argument("--interval", type=int, default=5, help="Poll interval in seconds (default: 5)")
    parser.add_argument("--timeout", type=int, default=300, help="Max wait time in seconds (default: 300)")
    args = parser.parse_args()

    api_key = args.api_key
    base_url = "https://pollo.ai/api/platform"
    if not api_key:
        try:
            config = load_config()
            api_key = config["api_key"]
            base_url = config.get("base_url", base_url)
        except (FileNotFoundError, ValueError) as e:
            print(json.dumps({"status": "error", "error": str(e)}))
            sys.exit(3)

    result = poll_task(args.task_id, api_key, base_url, args.interval, args.timeout)
    print(json.dumps(result, indent=2))

    status = result.get("status", "error")
    if status == "succeed":
        sys.exit(0)
    elif status == "failed":
        sys.exit(1)
    elif status == "timeout":
        sys.exit(2)
    else:
        sys.exit(3)


if __name__ == "__main__":
    main()
