def two_sum(nums,target):
    n=len(nums)
    seen={}
    for index,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [index,seen[complement]]
        seen[num]=index
print(sorted(two_sum([3,2,4],6)))
