def ispossible(nums,m,k,day):
    n=len(nums)
    ans=0
    cnt=0
    for i in nums:
        if i<=day:
            cnt+=1
        else:
            ans+=(cnt//k)
            cnt=0
    ans+=(cnt//k)
    return ans>=m
def makeboq(nums,m,k):
    if len(nums)<m*k:
        return -1
    left,right=min(nums),max(nums)
    ans1=right
    while left<=right:
        mid=(left+right)//2
        if(not ispossible(nums,m,k,mid)):
            left=mid+1
        else:
            ans1=mid
            right=mid-1
    return ans1
n = 8
nums = [7, 7, 7, 7, 13, 11, 12, 7]
m = 2
k = 3
print(makeboq(nums,m,k))
            
