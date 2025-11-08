def reverse_pair(nums):
    n=len(nums)
    cnt=0
    for i in range(n):
        for j in range(n):
            if nums[i]>2*nums[j]:
                cnt+=1
    return cnt
nums = [6, 4, 1, 2, 7]
print(reverse_pair(nums))
