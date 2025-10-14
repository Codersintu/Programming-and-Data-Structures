# 14/10/2025

# BFS code implementation in Python
def BFS(graph, start):
    visited = set()  
    visited.add(start) 
    queue = [start] 
    
    if not graph:
        print("Graph is empty")
        return      

    while queue:      
        vertex = queue.pop(0)
        print(vertex, end=" ")

        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# BFS(graph, 'A')


# DFS code implementation in Python
def DFS(graph, start):
    if not graph:
        print("Graph is empty")
        return

    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()    
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

DFS(graph, 'A')
  