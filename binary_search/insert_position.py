def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    ans = len(nums)  # default insertion at end
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return ans
nums = [1, 3, 5, 6]
target = 5
print(search_insert(nums,target))