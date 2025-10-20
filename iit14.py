class Graph:
    def __init__(self):
    
        self.graph = {}

    def add_vertex(self, vertex):
        
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print(f"Vertex '{vertex}' already exists.")

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)

        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def print_graph(self):
        """Print the adjacency list."""
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")


# Example usage
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.print_graph()
