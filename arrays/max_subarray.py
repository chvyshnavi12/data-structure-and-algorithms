def max_subarray(nums):
    n=len(nums)
    maxsum=0
    result=0
    for i in nums:
        maxsum=max(maxsum+i,i)
        result=max(maxsum,result)
    return result
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
