
# @Title: 两两交换链表中的节点 (Swap Nodes in Pairs)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:24:18
# @Runtime: 44 ms
# @Memory: 13.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        before_head = ListNode(next=head)
        pt = before_head
        while pt.next and pt.next.next:
            self.swapAdj(pt, pt.next, pt.next.next.next)
            pt = pt.next.next
        return before_head.next
        
    @staticmethod
    def swapAdj(left, start, right):
        end = start.next
        left.next = end
        start.next = right
        end.next = start
