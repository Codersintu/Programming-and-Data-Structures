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



# 09/10/2025
n=3 #number of vertices
adj_matrix=[[0]*n for _ in range(n)] # initialize 3*3 matrix with zeros

edges=[(0,1),(1,2),(2,0)]
for u,v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] =1 #because undirected graph

print("Adjacency Matrix (Undirected Graph)")
for row in adj_matrix:
    print(row)

n=3 # number of vertices
adj_matrix=[[0]*n for _ in range(n)] # initialize 3*3 matrix with zeros

edges=[(0,1),(1,2),(2,0)]
for u,v in edges:
    adj_matrix[u][v] = 1 #because directed graph

print("Adjacency Matrix (directed Graph)")
for row in adj_matrix:
    print(row)


n=3 # number of vertices
adj_list=[[] for _ in range(n)] # initialize 3*3 matrix with zeros

edges=[(0,1),(1,2),(2,0)]
for u,v in edges:
    adj_list[u].append(v) #because directed graph
    adj_list[v].append(u)
print("Adjacency list (Undirected Graph)")
for i in range(n):
    print(i,"->",adj_list[i])


n=3 # number of vertices
adj_list=[[] for _ in range(n)] # initialize 3*3 matrix with zeros

edges=[(0,1),(1,2),(2,0)]
for u,v in edges:
    adj_list[u].append(v) #because directed graph
    
print("Adjacency list (Undirected Graph)")
for i in range(n):
    print(i,"->",adj_list[i])


