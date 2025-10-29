class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head)
        length=0
        first=head
        while first:
            first=first.next
            length+=1
        length-=n
        second=dummy
        while length>0:
            second=second.next
            length-=1
        second.next=second.next.next
        return dummy.next
