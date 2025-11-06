def kadens_Subarr(nums):
    n=len(nums)
    max_sum=0
    start,end,s=0,0,0
    curr_sum=0
    for i in range(n):
        curr_sum+=nums[i]
        if curr_sum>max_sum:
            max_sum=curr_sum
            start=s
            end=i
        if curr_sum<0:
            start=i+1
            curr_sum=0
    return max_sum,nums[start:end+1]
nums=[2, 3, 5, -2, 7, -4]
print(kadens_Subarr(nums))
    
