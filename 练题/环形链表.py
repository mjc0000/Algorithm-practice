# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from unittest.result import failfast


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow=head
        fast=head.next
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast= not fast.next.next
        return True
