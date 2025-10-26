def max_product_subarray(nums):
    n=len(nums)
    min_arr=[0]*n
    max_arr=[0]*n
    min_arr[0]=nums[0]
    max_arr[0]=nums[0]
    for i in range(1,n):
        min_arr[i]=min(min_arr[i-1]*nums[i],nums[i],max_arr[i-1]*nums[i])
        max_arr[i]=max(min_arr[i-1]*nums[i],nums[i],max_arr[i-1]*nums[i])
    return max(max_arr)
print(max_product_subarray([2,3,-2,4]))