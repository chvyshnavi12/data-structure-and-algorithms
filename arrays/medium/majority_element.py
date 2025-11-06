from collections import Counter
def majority_element(nums):
    maxl=0
    counter=Counter(nums)
    for i in nums:
        result=counter[i]
        maxl=max(result,maxl)
    for i in nums:
        if counter[i]==maxl:
            return i
    
nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
print(majority_element(nums))






