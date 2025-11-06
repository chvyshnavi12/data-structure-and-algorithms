def union_of_array(num1,num2):
    nums=num1+num2
    result=[]
    for i in nums:
        if i not in result:
            result.append(i)
    return result
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
print(union_of_array(nums1,nums2))