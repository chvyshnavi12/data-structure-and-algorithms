def merge_intervals(nums):
    n=len(nums)
    merged=[]
    merged.append(nums[0])
    for start,end in nums:
        last_start,last_end=merged[-1]
        if start<=last_end:
            merged[-1][1]=max(end,last_end)
        else:
            merged.append([start,end])
    return merged
intervals = [[1,5],[3,6],[8,10],[15,18]]
print(merge_intervals(intervals))