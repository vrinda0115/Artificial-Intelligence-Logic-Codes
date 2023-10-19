graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B', 'G'],
    'E' : ['B', 'G'],
    'F' : ['C', 'H'],
    'G' : ['D','E','I'],
    'H' :['F', 'I'],
    'I' : ['H', 'G']
}

visited = []
queue = []

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m)

        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

print("following is the bfs ")
bfs(visited,graph,'A')        