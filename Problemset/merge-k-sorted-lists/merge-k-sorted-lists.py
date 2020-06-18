
# @Title: 合并K个排序链表 (Merge k Sorted Lists)
# @Author: allan.wanglz@qq.com
# @Date: 2020-06-18 22:24:10
# @Runtime: 104 ms
# @Memory: 17.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class FirstListNode():
    
    def __init__(self, a: ListNode):
        self.node = a
        
    def __lt__(self, other):
        return self.node.val < other.node.val
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [item for item in lists if item]
        if len(lists) == 0:
            return None
        first_lists = [FirstListNode(item) for item in lists]
        heapq.heapify(first_lists)
        head = ListNode()
        pt = head
        while len(first_lists):
            small_node = heapq.heappop(first_lists)
            pt.next = small_node.node
            pt = pt.next
            if pt.next is not None:
                heapq.heappush(first_lists, FirstListNode(pt.next))
        head = head.next
        return head
