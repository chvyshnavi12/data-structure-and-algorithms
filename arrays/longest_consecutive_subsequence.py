def lcs(nums):
    n=len(nums)
    nums.sort()
    cnt=1
    result=0
    for i in range(1,n):
        if nums[i]==nums[i-1]+1:
            cnt+=1
            result=max(result,cnt)
        else:
            cnt=1
    return result
print(lcs([100,4,200,1,3,2]))
        