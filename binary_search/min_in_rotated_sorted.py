def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid element > right element,
        # the min must be in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Min could be mid or to its left
            right = mid

    return nums[left]
