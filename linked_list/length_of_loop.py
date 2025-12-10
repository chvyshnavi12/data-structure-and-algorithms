class Solution:
    def findLengthOfLoop(self, head):
        fast = slow = head
        
        # Step 1: Detect cycle using Floyd’s Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # cycle detected
                break
        else:
            return 0  # No loop
        
        # Step 2: Count length of cycle
        count = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            count += 1
        
        return count
