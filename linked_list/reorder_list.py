class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: void. Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return 
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        prev=None
        slow.next=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        first=head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2


        
