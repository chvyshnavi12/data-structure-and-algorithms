def dfs(adj,s):
    n=len(adj)
    result=[]
    visited=[False]*n
    def helper(s):
        result.append(s)
        visited[s]=True
        for v in adj[s]:
            if not visited[v]:
                helper(v)
    helper(s)
    return result

if __name__ == "__main__":
    adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    ans = dfs(adj, 1)   # start DFS from node 3
    print(*ans)