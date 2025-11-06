def rotate_clock_wise(nums):
    n=len(nums)
    m=len(nums[0])
    for i in range(n):
        for j in range(i+1,n):
            nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
    for i in range(n):
        nums[i].reverse()
    return nums
nums=  [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
print(rotate_clock_wise(nums))