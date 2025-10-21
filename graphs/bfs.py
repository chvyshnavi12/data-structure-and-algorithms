def bfs(adj,s):
    result=[]
    from collections import deque
    q=deque()
    n=len(adj)
    visited=[False]*n
    visited[s]=True
    
    q.append(s)
    while q:
        curr=q.popleft()
        result.append(curr)
        for v in adj[curr]:
            if not visited[v] :
                visited[v]=True
                q.append(v)
    return result

if __name__ == "__main__":
    adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    ans = bfs(adj, 3)   # start BFS from node 3
    print(*ans)