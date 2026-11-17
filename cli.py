"""Command-line entry point for the utility functions in app.py."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from app import calculate_average, is_palindrome, normalize_whitespace, word_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="textutils", description="Text and number utilities.")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("normalize", help="collapse runs of whitespace").add_argument("text")
    commands.add_parser("wordcount", help="count whitespace-delimited words").add_argument("text")
    commands.add_parser("palindrome", help="check for a palindrome").add_argument("text")
    commands.add_parser("average", help="arithmetic mean of numbers").add_argument(
        "numbers", nargs="+", type=float
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "normalize":
            print(normalize_whitespace(args.text))
        elif args.command == "wordcount":
            print(word_count(args.text))
        elif args.command == "palindrome":
            print(is_palindrome(args.text))
        else:
            print(calculate_average(args.numbers))
    except (TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
