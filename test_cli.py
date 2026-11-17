"""Tests for the command-line entry point."""

import pytest

from cli import main


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        (["normalize", "  a   b "], "a b"),
        (["wordcount", "one two three"], "3"),
        (["palindrome", "racecar"], "True"),
        (["average", "2", "4"], "3.0"),
    ],
)
def test_commands_print_result(capsys, argv, expected):
    assert main(argv) == 0
    assert capsys.readouterr().out.strip() == expected


def test_invalid_numbers_return_error(capsys):
    assert main(["average", "inf"]) == 1
    assert "finite" in capsys.readouterr().err
