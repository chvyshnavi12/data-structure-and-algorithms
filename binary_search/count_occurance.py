def count_occ(nums,target):
    n=len(nums)
    left,right=0,n-1
    first,last=0,0
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            first=mid
            right=mid-1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            last=mid
            left=mid+1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return last-first+1
arr = [0, 0, 1, 1, 1, 2, 3]
target = 1
print(count_occ(arr,target))
    