"""
LeetCode 9: Palindrome Number

Given an integer x, return True if x is a palindrome (reads the same
forwards and backwards), and False otherwise.

Two approaches are included:
1. is_palindrome_string - converts to a string and checks reversal.
   Simple, O(n) time, O(n) space (for the string copies).
2. is_palindrome_math - reverses the number using arithmetic only,
   without converting to a string. This answers the problem's
   follow-up challenge. O(n) time, O(1) space.
"""


def is_palindrome_string(x: int) -> bool:
    """
    Check palindrome by converting to a string and comparing to its reverse.

    Args:
        x: the integer to check.

    Returns:
        True if x reads the same forwards and backwards, False otherwise.
    """
    # negative numbers can never be palindromes because of the '-' sign
    if x < 0:
        return False

    text = str(x)
    return text == text[::-1]


def is_palindrome_math(x: int) -> bool:
    """
    Check palindrome using only arithmetic - no string conversion.

    Builds a reversed version of x digit-by-digit, then compares it
    to the original.

    Args:
        x: the integer to check.

    Returns:
        True if x reads the same forwards and backwards, False otherwise.
    """
    # negative numbers can never be palindromes
    if x < 0:
        return False

    # numbers ending in 0 (except 0 itself) can't be palindromes,
    # since the reversed version would need a leading 0
    if x != 0 and x % 10 == 0:
        return False

    original = x
    reversed_number = 0

    while x > 0:
        last_digit = x % 10                       # pull off the last digit
        reversed_number = reversed_number * 10 + last_digit  # shift left, add it
        x = x // 10                                # strip that digit off

    return reversed_number == original


if __name__ == "__main__":
    # quick manual check when running this file directly
    print(is_palindrome_string(121))   # expected: True
    print(is_palindrome_string(-121))  # expected: False
    print(is_palindrome_string(10))    # expected: False

    print(is_palindrome_math(121))     # expected: True
    print(is_palindrome_math(-121))    # expected: False
    print(is_palindrome_math(10))      # expected: False