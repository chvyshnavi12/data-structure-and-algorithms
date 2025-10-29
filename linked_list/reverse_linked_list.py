class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        curr=head
        prev=None
        while curr:
            nextone=curr.next
            curr.next=prev
            prev=curr
            curr=nextone
        return prev

