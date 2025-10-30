def pacific_atlantic(heights):
    row=len(heights)
    col=len(heights)
    pacific=[[False]*col for _ in range(row)]
    atlantic=[[False]*col for _ in range(row)]
    def bfs(r,c,visited,prev_height):
        if r<0 or r>=row or c<0 or c>=col or visited[r][c] or heights[r][c]<prev_height:
            return
        visited[r][c]=True
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            bfs(r+dx,c+dy,visited,heights[r][c])
    for c in range(col):
        bfs(0,c,pacific,heights[0][c])
        bfs(row-1,c,atlantic,heights[row-1][c])
    for r in range(row):
        bfs(r,0,pacific,heights[r][0])
        bfs(r,col-1,atlantic,heights[r][col-1])
    result=[]
    for i in range(row):
        for j in range(col):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i,j])
    return result
heights= [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacific_atlantic(heights))

