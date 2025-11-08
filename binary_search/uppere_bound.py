def upper_bound(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    ans = n  # if no element > target, return n
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans
nums = [3,5,8,15,19]
x = 9
print(upper_bound(nums,x))
