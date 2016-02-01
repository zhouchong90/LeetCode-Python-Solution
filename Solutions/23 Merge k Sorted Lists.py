# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heapify, heapreplace, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        node = dummy
        heap = [(n.val,n) for n in lists if n]
        heapify(heap)
        while heap:
            i, n = heap[0]
            if not n.next:
                heappop(heap)
            else:
                heapreplace(heap,(n.next.val,n.next))
            node.next = n
            node = node.next
        return dummy.next