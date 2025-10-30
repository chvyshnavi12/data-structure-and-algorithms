def no_of_island(grid):
    n,m=len(grid),len(grid[0])
    cnt=0
    def dfs(i,j):
        if i<0 or i>=n or j<0 or j>=m or grid[i][j]=="0":
            return
        grid[i][j]="0"
        dfs(i,j+1),
        dfs(i+1,j),
        dfs(i-1,j),
        dfs(i,j-1)
    for i in range(n):
        for j in range(m):
            if grid[i][j]=="1":
                cnt+=1
                dfs(i,j)
    return cnt
grid1=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid=[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(no_of_island(grid))




