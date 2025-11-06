def leaders_in_arr(nums):
    n=len(nums)
    result=[]
    max_right=float("-inf")
    for i in range(n-1,-1,-1):
        if nums[i]>=max_right:
            result.append(nums[i])
            max_right=nums[i]
    result.reverse()
    return result
nums= [1, 2, 5, 3, 1, 2]
num1=[-3, 4, 5, 1, -4, -5]
print(leaders_in_arr(num1))