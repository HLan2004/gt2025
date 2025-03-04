import heapq

# Adjacency matrix representing the graph
graph = [
    [0, 4, float('inf'), float('inf'), 1, float('inf'), 2, float('inf'), float('inf')],
    [4, 0, 7, float('inf'), float('inf'), 5, float('inf'), float('inf'), float('inf')],
    [float('inf'), 7, 0, 1, float('inf'), 8, float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 1, 0, float('inf'), 6, 4, 3, float('inf')],
    [1, float('inf'), float('inf'), float('inf'), 0, 9, 10, float('inf'), float('inf')],
    [float('inf'), 5, 8, 6, 9, 0, float('inf'), float('inf'), 2],
    [2, float('inf'), float('inf'), 4, 10, float('inf'), 2, float('inf'), 8],
    [float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, 8, 1, 0]
]


# Prim's algorithm function
def prim(graph, root):
    num_nodes = len(graph)
    mst_edges = []
    visited = [False] * num_nodes
    min_heap = [(0, root, -1)]  # (weight, current_node, parent_node)
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        total_weight += weight
        if parent != -1:
            mst_edges.append((parent + 1, node + 1, weight))  # Convert to 1-based index

        for adj in range(num_nodes):
            if not visited[adj] and graph[node][adj] != float('inf'):
                heapq.heappush(min_heap, (graph[node][adj], adj, node))

    return mst_edges, total_weight


# Input the root node
root_node = int(input("Enter the root node (1-9): ")) - 1  # 1-based to 0-based index

mst_edges, total_weight = prim(graph, root_node)
print("\nPrim's Algorithm - MST edges and weights:")
for edge in mst_edges:
    print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total weight of MST: {total_weight}")


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False


# Kruskal's algorithm function
def kruskal(graph):
    num_nodes = len(graph)
    edges = []
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if graph[i][j] != float('inf'):
                edges.append((graph[i][j], i, j))  # (weight, node1, node2)

    # Sort edges by weight
    edges.sort()

    uf = UnionFind(num_nodes)
    mst_edges = []
    total_weight = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((u + 1, v + 1, weight))  # Convert to 1-based index
            total_weight += weight

    return mst_edges, total_weight


# Kruskal's algorithm result
mst_edges_kruskal, total_weight_kruskal = kruskal(graph)
print("\nKruskal's Algorithm - MST edges and weights:")
for edge in mst_edges_kruskal:
    print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
print(f"Total weight of MST: {total_weight_kruskal}")