def min_rotated_sorted(nums):
    n=len(nums)
    left=0
    right=n-1

    while left<=right:
        mid=(left+right)//2
        if nums[left]>=nums[mid] and nums[right]>=nums[mid]:
            return nums[mid]
        elif nums[left]<nums[mid]:
            left=mid
        else:
            right=mid
    return -1
print(min_rotated_sorted([5,6,1,2,3]))
