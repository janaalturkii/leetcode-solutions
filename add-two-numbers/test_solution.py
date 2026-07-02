"""
Tests for the add_two_numbers solution.
Covers the standard examples plus edge cases: carry overflow,
different-length lists, and zero.
"""

from solution import add_two_numbers, list_to_linked_list, linked_list_to_list


def test_example_1():
    # 342 + 465 = 807
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [7, 0, 8]


def test_both_lists_empty_digit_zero():
    # 0 + 0 = 0
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [0]


def test_carry_creates_extra_digit():
    # 9999999 + 9999 = 10009998, tests carry propagating an extra digit
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_different_length_lists():
    # 99 + 1 = 100, second list is shorter
    l1 = list_to_linked_list([9, 9])
    l2 = list_to_linked_list([1])
    result = add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [0, 0, 1]


def test_single_digit_no_carry():
    # 2 + 3 = 5, simplest possible case
    l1 = list_to_linked_list([2])
    l2 = list_to_linked_list([3])
    result = add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [5]


def test_final_carry_adds_new_node():
    # 5 + 5 = 10, sum has one more digit than either input
    l1 = list_to_linked_list([5])
    l2 = list_to_linked_list([5])
    result = add_two_numbers(l1, l2)
    assert linked_list_to_list(result) == [0, 1]