def countRotations(nums):
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    # 'left' now points to the smallest element
    return left
