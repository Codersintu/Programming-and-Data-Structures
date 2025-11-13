from collections import defaultdict, deque



def build_adj_list(n, edges):
    graph = defaultdict(list)

    for u, v, w in edges:    
        graph[u].append((v, w))
        graph[v].append((u, w)) 

    return graph



def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    bfs_order = []

    while queue:
        city = queue.popleft()
        bfs_order.append(city)

        for neighbor, cost in graph[city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order



n = int(input())


e = int(input())

edges = []
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

graph = build_adj_list(n, edges)

print("\nAdjacency List:")
for city in graph:
    print(city, ":", graph[city])

bfs_result = bfs(graph, 0)

print("\nBFS Traversal starting from City 0:")
print(bfs_result)
