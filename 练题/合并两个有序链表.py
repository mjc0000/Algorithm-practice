# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        current=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                current.next=list2
                list2=list2.next
            else:
                current.next=list1
                list1=list1.next

        if list1:
            current.next=list1
        if list2:
            current.next=list2

        return dummy.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:  # 修正：使用 <= 确保升序
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # 移动 current 指针（虽然不影响正确性，但更规范）

        # 连接剩余节点（保持不变）
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next
