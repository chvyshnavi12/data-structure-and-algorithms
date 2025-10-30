class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

def build_graph(adjList):
    if not adjList:
        return None
    nodes = [Node(i + 1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbours = [nodes[j - 1] for j in neighbors]
    return nodes[0]

def clone_graph(node):
    old_to_new = {}

    def dfs(curr):
        if curr in old_to_new:
            return old_to_new[curr]

        copy = Node(curr.val)
        old_to_new[curr] = copy

        for nei in curr.neighbours:
            copy.neighbours.append(dfs(nei))
        return copy

    return dfs(node) if node else None

def graph_to_adjList(node):
    if not node:
        return []
    visited = {}
    def dfs(curr):
        if curr.val in visited:
            return
        visited[curr.val] = [n.val for n in curr.neighbours]
        for nei in curr.neighbours:
            dfs(nei)
    dfs(node)
    return [visited[i] for i in sorted(visited.keys())]

# Example
adjList = [[2,4],[1,3],[2,4],[1,3]]
original = build_graph(adjList)
cloned = clone_graph(original)
print(graph_to_adjList(cloned))
