def rotate_array(nums,k):
    n=len(nums)
    list1=nums[n-k:]
    list2=nums[:n-k]
    return list1+list2
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate_array(nums,k))