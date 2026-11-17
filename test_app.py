"""Unit tests for the sample application's utility functions."""

import math

import pytest

from app import calculate_average, is_palindrome, normalize_whitespace, word_count


class TestNormalizeWhitespace:
    @pytest.mark.parametrize(
        ("source", "expected"),
        [
            ("", ""),
            (" \t\n ", ""),
            ("hello", "hello"),
            ("  hello\tworld\n!  ", "hello world !"),
            ("one\u00a0two", "one two"),
        ],
    )
    def test_collapses_whitespace(self, source, expected):
        assert normalize_whitespace(source) == expected

    @pytest.mark.parametrize("value", [None, 42, ["hello"]])
    def test_rejects_non_string_input(self, value):
        with pytest.raises(TypeError, match="text must be a string"):
            normalize_whitespace(value)


class TestWordCount:
    @pytest.mark.parametrize(
        ("text", "expected"),
        [
            ("", 0),
            (" \n\t ", 0),
            ("one", 1),
            ("one two three", 3),
            ("  one,\ttwo!  ", 2),
        ],
    )
    def test_counts_whitespace_delimited_words(self, text, expected):
        assert word_count(text) == expected

    def test_rejects_non_string_input(self):
        with pytest.raises(TypeError, match="text must be a string"):
            word_count(10)


class TestIsPalindrome:
    @pytest.mark.parametrize(
        "text",
        ["", "a", "racecar", "A man, a plan, a canal: Panama!", "No 'x' in Nixon"],
    )
    def test_recognizes_palindromes_by_default(self, text):
        assert is_palindrome(text)

    @pytest.mark.parametrize("text", ["python", "hello", "abca"])
    def test_rejects_non_palindromes(self, text):
        assert not is_palindrome(text)

    def test_can_make_case_sensitive(self):
        assert is_palindrome("Aa")
        assert not is_palindrome("Aa", ignore_case=False)

    def test_can_include_punctuation_and_whitespace(self):
        assert is_palindrome("a,b")
        assert not is_palindrome("a,b", alphanumeric_only=False)
        assert not is_palindrome("a a", alphanumeric_only=False)

    @pytest.mark.parametrize("option", ["yes", 1, None])
    def test_rejects_non_boolean_options(self, option):
        with pytest.raises(TypeError, match="ignore_case must be a bool"):
            is_palindrome("aba", ignore_case=option)
        with pytest.raises(TypeError, match="alphanumeric_only must be a bool"):
            is_palindrome("aba", alphanumeric_only=option)

    def test_rejects_non_string_input(self):
        with pytest.raises(TypeError, match="text must be a string"):
            is_palindrome(None)


class TestCalculateAverage:
    def test_calculates_average_of_integers(self):
        assert calculate_average([2, 4, 6]) == 4.0

    def test_calculates_average_of_mixed_real_numbers(self):
        assert calculate_average((1, 2.5, -0.5)) == pytest.approx(1.0)

    def test_accepts_a_generator_and_consumes_it_once(self):
        assert calculate_average(number for number in range(1, 5)) == 2.5

    def test_accepts_a_single_value(self):
        assert calculate_average([7]) == 7.0

    def test_rejects_non_iterable_input(self):
        with pytest.raises(TypeError, match="values must be an iterable"):
            calculate_average(3)

    @pytest.mark.parametrize("values", [[], iter(())])
    def test_rejects_empty_iterable(self, values):
        with pytest.raises(ValueError, match="values must not be empty"):
            calculate_average(values)

    @pytest.mark.parametrize("value", ["1", None, True, False, 1j])
    def test_rejects_non_real_values_and_booleans(self, value):
        with pytest.raises(TypeError, match="values must contain only real numbers"):
            calculate_average([value])

    @pytest.mark.parametrize("value", [math.inf, -math.inf, math.nan])
    def test_rejects_non_finite_values(self, value):
        with pytest.raises(ValueError, match="values must contain only finite numbers"):
            calculate_average([value])
