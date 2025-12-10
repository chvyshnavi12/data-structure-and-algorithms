class Solution:
    def deleteAllOccurrences(self, head, target):
        if not head:
            return head

        curr = head

        # 1. Delete target nodes at head
        while curr and curr.val == target:
            curr = curr.next
            if curr:
                curr.prev = None
            head = curr

        # 2. Delete target nodes after head
        while curr:
            if curr.val == target:
                # Remove curr
                prev_node = curr.prev
                next_node = curr.next

                prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node

                curr = next_node
            else:
                curr = curr.next

        return head
