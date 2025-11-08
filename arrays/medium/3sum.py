def sum3(nums):
    n=len(nums)
    result=[]
    nums.sort()
    for i in range(n):
        left=i+1
        right=n-1
        while left<=right:
            target=nums[left]+nums[i]+nums[right]
            if target==0:
                result.append([nums[left],nums[right],nums[i]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
            left+=1
            right-=1
    return result
nums=[0,1,1]
print(sum3(nums))
