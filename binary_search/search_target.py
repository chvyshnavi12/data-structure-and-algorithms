def search(nums,target):
    n=len(nums)
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return True
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return False
nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))