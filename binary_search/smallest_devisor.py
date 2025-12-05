import math
def check(nums,limit,k):
    n=len(nums)
    ans=0
    for i in nums:
        ans+=math.ceil(i/k)
    return ans<=limit
def smallest_divisor(nums,limit):
    n=len(nums)
    left,right=1,max(nums)
    x=right
    while left<=right:
        mid=(left+right)//2
        if(check(nums,limit,mid)):
            x=mid
            right=mid-1
        else:
            left=mid+1
    return x
nums = [1, 2, 3, 4, 5]
limit = 8
print(smallest_divisor(nums,limit))
