import math
def findpile(nums,h,k):
    n=len(nums)
    ans=0
    for i in nums:
        ans=ans+math.ceil(i/k)
    if ans<=k:
        return True
    return False
def kokobanana(nums,h):
    left,right=0,len(nums)-1
    minimum=float("inf")
    
    while left<=right:
        mid=(left+right)//2
        if(findpile(nums,h,nums[mid]) and nums[mid]<minimum):
            minimum=nums[mid]
            right=mid-1
        elif nums[mid]>h:
            left=mid+1
        else:
            right=mid-1
    return minimum
n = 4
nums = [7, 15, 6, 3]
h = 10
print(kokobanana(nums,h))
        


        