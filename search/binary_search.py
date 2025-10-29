def binary_search(nums,target):
    n=len(nums)
    left=0
    right=n-1
    while left<=right:
        mid=left+right//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid
    return -1
print(binary_search([2,3,4,5,6],3))