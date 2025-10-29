def product_array(nums):
    n=len(nums)
    result=[1]*n
    prefix=1
    for i in range(n):
        result[i]=prefix
        prefix*=nums[i]
    suffix=1
    for i in range(n-1,-1,-1):
        result[i]*=suffix
        suffix*=nums[i]
    return result
print(product_array([1,2,3,4]))
