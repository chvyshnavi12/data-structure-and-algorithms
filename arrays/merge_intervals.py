def merge_intervals(nums):
    n=len(nums)
    merged=[]
    last_start,last_end=nums[0]
    merged.append([last_start,last_end])
    for start,end in nums:
        if start<last_end:
            merged[-1][1]=max(end,last_end)
        else:
            merged.append([start,end])
    return merged
nums=[[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(nums))