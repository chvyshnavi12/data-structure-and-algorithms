class Solution:
    def findPairsWithGivenSum(self, head, target):
        if not head:
            return []

        # Step 1: find tail of DLL
        left = head
        right = head
        while right.next:
            right = right.next

        result = []

        # Step 2: two pointer traversal
        while left != right and right.next != left:
            s = left.val + right.val

            if s == target:
                result.append([left.val, right.val])
                left = left.next
                right = right.prev

            elif s < target:
                left = left.next
            else:
                right = right.prev

        return result
