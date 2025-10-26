def find_duplicate(nums):
    n=len(nums)
    seen=set()
    result=[]
    for i in nums:
        if i in seen:
            result.append(i)
        seen.add(i)
    return result
print(find_duplicate([1,3,3,4,2,2]))