

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1




def kruskal_forest(V, edges):
   
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(V)
    forest = []   

    for u, v, w in edges:
     
        if ds.find(u) != ds.find(v):
            forest.append((u, v, w))
            ds.union(u, v)

    return forest




V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

forest = kruskal_forest(V, edges)

print("Minimum Spanning Forest:")
total_cost = 0

for u, v, w in forest:
    print(f"{u} - {v} : {w}")
    total_cost += w

print("Total Cost:", total_cost)
