"""
LeetCode 2: Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each node
contains a single digit. Add the two numbers and return the sum as a
linked list, in the same reversed-digit format.

Approach: simulate grade-school addition, one digit (node) at a time,
carrying over into the next digit when a sum reaches 10 or more.
Time complexity: O(max(n, m)), where n and m are the lengths of the
two input lists - we visit each node at most once.
"""

from typing import Optional


class ListNode:
    """A single node in a singly linked list."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Add two numbers represented as reversed-digit linked lists.

    Args:
        l1: head node of the first number's linked list.
        l2: head node of the second number's linked list.

    Returns:
        Head node of a new linked list representing the sum, also in
        reversed-digit order.
    """
    dummy_head = ListNode()  # placeholder so we don't special-case the first node
    current = dummy_head
    carry = 0

    # keep going while either list still has digits, or there's a leftover carry
    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        column_sum = digit1 + digit2 + carry
        carry = column_sum // 10       # tens digit becomes next carry
        digit_to_store = column_sum % 10  # ones digit becomes this node's value

        current.next = ListNode(digit_to_store)
        current = current.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return dummy_head.next  # skip the placeholder


def list_to_linked_list(values: list[int]) -> Optional[ListNode]:
    """Helper: build a linked list from a Python list, e.g. [2,4,3]."""
    dummy_head = ListNode()
    current = dummy_head
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy_head.next


def linked_list_to_list(node: Optional[ListNode]) -> list[int]:
    """Helper: convert a linked list back into a Python list, for easy checking."""
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    # quick manual check when running this file directly
    l1 = list_to_linked_list([2, 4, 3])  # represents 342
    l2 = list_to_linked_list([5, 6, 4])  # represents 465
    result = add_two_numbers(l1, l2)
    print(linked_list_to_list(result))  # expected: [7, 0, 8]  (807)