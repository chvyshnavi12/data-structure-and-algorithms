def remove_duplicates(nums):
    result=[]
    for i in nums:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicates([0,0,3,3,4]))