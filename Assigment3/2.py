from collections import defaultdict


def dfs(node, graph, visited, component):
    visited.add(node)
    component.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, component)



if __name__ == "__main__":
    
    n, e = map(int, input().split()) 

    graph = defaultdict(list)

    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = []


    for node in range(n):
        if node not in visited:
            component = []
            dfs(node, graph, visited, component)
            components.append(component)


    for i, comp in enumerate(components, start=1):
        print(f"Component {i}: {comp}")
