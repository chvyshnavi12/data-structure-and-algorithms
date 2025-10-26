def rotate_array(nums,k):
    n=len(nums)
    l1=nums[:k+1]
    l2=nums[k+1:]
    return l2+l1
print(rotate_array([1,2,3,4,5,6,7],3))