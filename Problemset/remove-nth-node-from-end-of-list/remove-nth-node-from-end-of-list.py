
# @Title: 删除链表的倒数第N个节点 (Remove Nth Node From End of List)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:23:32
# @Runtime: 44 ms
# @Memory: 13.8 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start, end = head, head
        while(n):
            end = end.next
            n -= 1
        if end is None:
            return start.next
        while end.next is not None:
            start = start.next
            end = end.next
        start.next = start.next.next
        return head
