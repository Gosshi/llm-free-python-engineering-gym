"""Small, reproducible entry point for the active challenge."""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHALLENGE = ROOT / "challenges" / "001-diagnostic-api"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run challenge 001 helper commands.")
    parser.add_argument("command", choices=("start", "test", "lint"))
    args = parser.parse_args()

    if args.command == "start":
        print("Challenge 001 is ready.")
        print(f"Start time (local): {datetime.now().astimezone().isoformat(timespec='seconds')}")
        print("Set a 90-minute timer and record this time in submission-notes.md.")
        print(f"Read: {CHALLENGE / 'README.md'}")
        return 0

    if args.command == "test":
        command = [sys.executable, "-m", "pytest"]
    else:
        command = [sys.executable, "-m", "ruff", "check", "."]
    return subprocess.run(command, cwd=ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
