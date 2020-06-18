
# @Title: K 个一组翻转链表 (Reverse Nodes in k-Group)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:24:24
# @Runtime: 68 ms
# @Memory: 14.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        before_head = ListNode(next=head)
        pt = before_head
        pt, head = self.swapAdjK(pt, head, k)
        while head is not None:
            pt, head = self.swapAdjK(pt, head, k)
        return before_head.next
        
    @staticmethod
    def swapAdjK(left, head, k):
        node_list = []
        while head is not None and k > 0:
            node_list.append(head)
            head = head.next
            k -= 1
        if k > 0:
            return None, None
        end = head
        node_pt = node_list.pop()
        left.next = node_pt
        while node_list:
            x = node_list.pop()
            node_pt.next = x
            node_pt = x
        node_pt.next = end
        return node_pt, end
