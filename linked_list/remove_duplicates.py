# Definition for doubly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        if not head:
            return head
        
        curr = head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                # duplicate found
                nextnode = curr.next.next
                
                # unlink the duplicate node
                curr.next.next = None     # for safety
                curr.next = nextnode      # skip duplicate
                
                if nextnode:
                    nextnode.prev = curr  # fix prev pointer
            else:
                curr = curr.next
        
        return head
