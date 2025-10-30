def max_product_subarray(nums):
    n=len(nums)
    min_box=[0]*n
    max_box=[0]*n
    min_box[0]=nums[0]
    max_box[0]=nums[0]
    for i in range(1,n):
        min_box[i]=min(min_box[i-1]*nums[i],max_box[i-1]*nums[i],nums[i])
        max_box[i]=max(min_box[i-1]*nums[i],max_box[i-1]*nums[i],nums[i])
    return max(max_box)
print(max_product_subarray([2,3,-2,4]))

