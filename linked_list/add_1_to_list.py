# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Reverse a linked list
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addOne(self, head):
        # Step 1: reverse
        head = self.reverse(head)

        # Step 2: add one
        curr = head
        carry = 1
        while curr:
            s = curr.val + carry
            curr.val = s % 10
            carry = s // 10
            
            # if no carry left, break early
            if carry == 0:
                break

            # if carry and next is None → add new node
            if curr.next is None and carry:
                curr.next = ListNode(1)
                carry = 0
                break

            curr = curr.next

        # Step 3: reverse back
        head = self.reverse(head)
        return head
