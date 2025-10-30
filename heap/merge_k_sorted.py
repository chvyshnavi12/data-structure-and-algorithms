import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        minheap=[]
        for node in lists:
            if node:
                heapq.heappush(minheap,(node.val,id(node),node))
        dummy=ListNode(0)
        curr=dummy
        while minheap:
            val, _,smallest=heapq.heappop(minheap)
            curr.next=smallest
            curr=curr.next
            if smallest.next:
                heapq.heappush(minheap,(smallest.next.val,id(smallest.next),smallest.next))
        return dummy.next
