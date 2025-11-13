import sys

def prim_mst(graph, V):
    INF = sys.maxsize
    selected = [False] * V
    edge_count = 0
    selected[0] = True  
    total_cost = 0

    print("Edges in MST:")

    while edge_count < V - 1:
        minimum = INF
        x = 0
        y = 0


        for i in range(V):
            if selected[i]: 
                for j in range(V):
                    if (not selected[j]) and graph[i][j] != 0:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y} : {graph[x][y]}")
        total_cost += graph[x][y]
        selected[y] = True
        edge_count += 1

    print("Total Cost of MST:", total_cost)



V = int(input())
graph = []

for _ in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

prim_mst(graph, V)
