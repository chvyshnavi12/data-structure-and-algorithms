from collections import Counter
def single_num(nums):
    n=len(nums)
    nums.sort()
    counter=Counter(nums)
    for i in nums:
        if counter[i]==1:
            return i
nums = [1, 2, 2, 4, 3, 1, 4]
print(single_num(nums))
