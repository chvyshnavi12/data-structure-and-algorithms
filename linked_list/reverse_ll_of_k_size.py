# Definition for singly linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev_group_end = dummy
        
        while True:
            kth = prev_group_end
            # find Kth node
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next   # not enough nodes at end
            
            group_start = prev_group_end.next
            next_group_start = kth.next

            # reverse nodes from group_start to kth
            prev = next_group_start
            curr = group_start
            
            while curr != next_group_start:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # connect reversed part to previous part
            prev_group_end.next = kth
            prev_group_end = group_start
