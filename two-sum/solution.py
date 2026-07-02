"""
LeetCode 1: Two Sum

Given an array of integers nums and an integer target, return the
indices of the two numbers that add up to target.

Approach: single-pass hash map.
As we walk through the list, we ask "have I already seen the number
that would complete this pair?" using a dictionary of {number: index}.
This gives O(n) time instead of the O(n^2) brute-force approach.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of the two numbers in nums that add up to target.

    Args:
        nums: list of integers to search.
        target: the sum we're looking for.

    Returns:
        A list of two indices [i, j] such that nums[i] + nums[j] == target.

    Raises:
        ValueError: if no valid pair is found (shouldn't happen per
        problem constraints, but included for safety/clarity).
    """
    seen: dict[int, int] = {}  # maps number -> its index

    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index

    raise ValueError("No two sum solution exists for the given input.")


if __name__ == "__main__":
    # quick manual check when running this file directly
    print(two_sum([2, 7, 11, 15], 9))  # expected: [0, 1]
    print(two_sum([3, 2, 4], 6))       # expected: [1, 2]
    print(two_sum([3, 3], 6))          # expected: [0, 1]