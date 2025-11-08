def lower_bound(nums,target):
    n=len(nums)
    left=0
    right=n-1
    ans=n
    while(left<=right):
        mid=(left+right)//2
        if nums[mid]>=target:
            ans=mid
            right=mid-1  
        else:
            left=mid+1
    return ans
nums= [3,5,8,15,19]
x = 9
print(lower_bound(nums,x))
    