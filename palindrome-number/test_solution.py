"""
Tests for both palindrome-number solutions.
Runs the same test cases against both implementations to confirm
they agree, plus edge cases: negatives, trailing zero, single digit, zero.
"""

import pytest
from solution import is_palindrome_string, is_palindrome_math


@pytest.mark.parametrize("solution_func", [is_palindrome_string, is_palindrome_math])
class TestPalindromeNumber:
    """Both implementations must pass the exact same set of cases."""

    def test_example_1_positive_palindrome(self, solution_func):
        assert solution_func(121) is True

    def test_example_2_negative_number(self, solution_func):
        assert solution_func(-121) is False

    def test_example_3_trailing_zero(self, solution_func):
        assert solution_func(10) is False

    def test_single_digit_is_always_palindrome(self, solution_func):
        assert solution_func(7) is True

    def test_zero_is_a_palindrome(self, solution_func):
        assert solution_func(0) is True

    def test_even_length_palindrome(self, solution_func):
        assert solution_func(1221) is True

    def test_even_length_non_palindrome(self, solution_func):
        assert solution_func(1223) is False

    def test_large_non_palindrome(self, solution_func):
        assert solution_func(123456789) is False