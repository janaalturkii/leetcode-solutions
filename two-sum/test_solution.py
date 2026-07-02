"""
Tests for the two_sum solution.
Covers the examples from the problem plus edge cases.
"""

import pytest
from solution import two_sum


def test_example_1():
    # basic case from the problem statement
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_example_2():
    # pair is not at the start of the list
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_example_3():
    # duplicate numbers that together form the answer
    assert two_sum([3, 3], 6) == [0, 1]


def test_minimum_length_list():
    # smallest allowed input: exactly 2 numbers
    assert two_sum([1, 2], 3) == [0, 1]


def test_negative_numbers():
    # negative numbers should work the same as positive ones
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_zero_in_list():
    # zero is a valid number in nums
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]


def test_answer_order_does_not_matter():
    # the problem says order of returned indices doesn't matter,
    # but our implementation always returns [first_index, second_index]
    result = two_sum([5, 75, 25], 100)
    assert sorted(result) == [1, 2]