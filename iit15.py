16/10/2025
from collections import deque

def connectedBfs(graph):
    visited = set()
    queue = deque()

    start_vertex = next(iter(graph))
    queue.append(start_vertex)
    visited.add(start_vertex)

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) == len(graph)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print(connectedBfs(graph))
