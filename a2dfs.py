graph = {
    'A' : set(['B', 'C']),
    'B' : set(['A', 'D', 'E']),
    'C' : set(['A', 'F']),
    'D' : set(['B']),
    'E' : set(['B', 'F']),
    'F' : set(['C', 'E'])
}

visited = set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for n in graph[root]:
            dfs(visited,graph,n)

dfs(visited,graph,'A')
