def container_with_water(nums):
    n=len(nums)
    left=0
    right=n-1
    max_sum=0
    if n==2:
        return max(nums[left],nums[right])
    while left<right:
        result=min(nums[left],nums[right])*(right-left)
        max_sum=max(result,max_sum)
        if nums[left]<nums[right]:
            left+=1
        else:
            right-=1

    return max_sum
print(container_with_water([1,8,6,2,5,4,8,3,7]))
