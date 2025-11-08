def count_inversion(nums):
    n=len(nums)
    cnt=0
    for i in range(n-1):
        for j in range(i,n):
            if nums[i]>nums[j]:
                cnt+=1
    return cnt
nums = [2, 3, 7, 1, 3, 5]
print(count_inversion(nums))