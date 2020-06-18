
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:23:51
# @Runtime: 56 ms
# @Memory: 13.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        start = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                start.next = l2
                l2 = l2.next
            elif l2 is None:
                start.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    start.next = l1
                    l1 = l1.next
                else:
                    start.next = l2
                    l2 = l2.next
            start = start.next
        return head.next
