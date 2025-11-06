def second_largest(nums):
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]>nums[1]:
        largest=nums[0]
        second=nums[1]
    else:
        largest=nums[1]
        second=nums[0]
    for i in range(2,n):
        if nums[i]>largest:
            second=largest
            largest=nums[i]
        elif(nums[i]>second and nums[i]!=largest):
            second=nums[i]
    return second
nums=[1,2,3,4,5]
print(second_largest(nums))