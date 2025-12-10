# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # three dummy heads
        zeroD = ListNode(0)
        oneD = ListNode(0)
        twoD = ListNode(0)

        # three tails
        zero = zeroD
        one = oneD
        two = twoD

        # distribute nodes into 0s,1s,2s lists
        curr = head
        while curr:
            if curr.val == 0:
                zero.next = curr
                zero = zero.next
            elif curr.val == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next

        # Now join the lists
        # 0's → 1's → 2's
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None   # very important to avoid cycle

        # head of new list
        return zeroD.next
