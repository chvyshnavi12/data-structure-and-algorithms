from collections import Counter
def majority_element(nums):
    n=len(nums)
    result=[]
    seen=set()
    counter=Counter(nums)
    for i in nums:
        if counter[i]>(n/3) and i not in seen:
            result.append(i)
            seen.add(i)
    return result
nums =[1, 2, 1, 1, 3, 2]
print(majority_element(nums))

