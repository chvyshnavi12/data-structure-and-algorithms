def course_sheduling(n,preq):
    graph={i:[] for i in range(n)}
    for a,b in preq:
        graph[a].append(b)
    visited=[0]*n
    def dfs(course):
        if visited[course]==1:
            return False
        if visited[course]==2:
            return True
        visited[course]=1
        for nei in graph[course]:
            if not dfs(nei):
                return False
        visited[course]=2
        return True
    for course in range(n):
        if not dfs(course):
            return False
    return True
nu=2
prequ=[[1,0]]
print(course_sheduling(nu,prequ))
