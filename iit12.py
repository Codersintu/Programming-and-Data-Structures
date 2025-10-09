7/10/2025
# Graph
# Adjacency Matrix for Undirected Graph
vertexData=['A','B','C','D']

adjacency_matrix=[
    [0,1,1,1], # Edges for A
    [1,0,1,0], # Edges for B
    [1,1,0,1], # Edges for c
    [1,0,0,0], # Edges for D
]

def print_adjacacency_matrix(matrix):
    print("\n adjacencecy Matrix")
    for row in matrix:
        print(row)


def print_connections(vertexData, matrix):
    print("\nConnections between vertices:")
    for i in range(len(vertexData)):
        connections = []
        for j in range(len(vertexData)):
            if matrix[i][j] == 1:
                connections.append(vertexData[j])
        print(f"{vertexData[i]} is connected to {', '.join(connections)}")

print("vertexData",vertexData)
print_adjacacency_matrix(adjacency_matrix)
