def first_last_occ(nums,target):
    n=len(nums)
    left=0
    right=n-1
    first=0
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
    last=0
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            last=mid
            left=mid+1
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return first,last
nums =[5, 7, 7, 8, 8, 10]
target = 8
print(first_last_occ(nums,target))


