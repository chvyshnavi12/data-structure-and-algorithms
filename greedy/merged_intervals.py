def merged_intervals(nums):
    n=len(nums)
    merged=[]
    merged.append(nums[0])
    for start,end in nums:
        last_start,last_end=merged[-1]
        if start<last_end:
            merged[-1][1]=max(last_end,end)
        else:
            merged.append([start,end])
    return merged
nums=[[1,3],[2,6],[8,10],[15,18]]
print(merged_intervals(nums))