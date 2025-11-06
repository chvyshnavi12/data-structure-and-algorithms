def matrixzero(nums):
    n=len(nums)
    row=set()
    col=set()
    for i in range(n):
        for j in range(n):
            if nums[i][j]==0:
                row.add(i)
                col.add(j)
    for i in range(n):
        for j in range(n):
            if i in row or j in col:
                nums[i][j]=0
    return nums
nums =[[1,1,1],[1,0,1],[1,1,1]]
print(matrixzero(nums))