# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # Dummy node initialization to handle edge cases more easily
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move prev to the node just before the left-th node
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing from this point
        reverse_start = prev.next
        curr = reverse_start.next

        # Reverse the sublist from left to right
        for _ in range(right - left):
            reverse_start.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = reverse_start.next

        return dummy.next
