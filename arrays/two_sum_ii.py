def two_sum(nums,target):
    n=len(nums)
    left=0
    right=n-1
    while left<=right:
        num_sum=nums[left]+nums[right]
        if num_sum==target:
            return [left+1,right+1]
        if num_sum<target:
            left+=1
        else:
            right-=1
print(two_sum([2,7,11,15],9))