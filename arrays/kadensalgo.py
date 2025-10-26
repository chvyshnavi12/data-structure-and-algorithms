def kadensalgo(nums):
    n=len(nums)
    result=nums[0]
    maxsum=nums[0]
    for i in nums:
        result=max(i,result+i)
        maxsum=max(result,maxsum)
    return maxsum
arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print(kadensalgo(arr))

