# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        
        for i in range(n):
            first = first.next
        
        while first.next is not None:
            first = first.next
            second = second.next
        else:
            second.next = second.next.next
        
        return dummy.next