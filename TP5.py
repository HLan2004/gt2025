import sys
import heapq

# Define the graph nodes and weighted edges
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "L", "M"]
graph_edges = {
    ("A", "B"): 4, ("A", "C"): 1, ("B", "F"): 3, ("C", "D"): 8,
    ("C", "F"): 7, ("D", "H"): 5, ("E", "F"): 1, ("E", "H"): 2,
    ("E", "L"): 2, ("F", "H"): 1, ("H", "G"): 3, ("H", "M"): 7,
    ("H", "L"): 6, ("G", "M"): 4, ("G", "L"): 4, ("L", "M"): 1
}

def build_adjacency_matrix(node_list, edge_info):
    num_nodes = len(node_list)
    mapping = {node: i for i, node in enumerate(node_list)}
    matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    
    
    for i in range(num_nodes):
        matrix[i][i] = 0

    for (u, v), cost in edge_info.items():
        i_u = mapping[u]
        i_v = mapping[v]
        matrix[i_u][i_v] = cost
        matrix[i_v][i_u] = cost  

    return matrix, mapping

def dijkstra_shortest_route(matrix, mapping, start, end):
    n = len(matrix)
    distances = [float('inf')] * n
    predecessors = [None] * n
    start_index = mapping[start]
    end_index = mapping[end]
    distances[start_index] = 0

    queue = [(0, start_index)]
    while queue:
        curr_distance, curr_index = heapq.heappop(queue)
        if curr_index == end_index:
            break
        if curr_distance > distances[curr_index]:
            continue

        for neighbor in range(n):
            weight = matrix[curr_index][neighbor]
            if weight < float('inf'):
                new_distance = curr_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = curr_index
                    heapq.heappush(queue, (new_distance, neighbor))
    
    
    route = []
    current = end_index
    while current is not None:
        route.append(current)
        current = predecessors[current]
    route.reverse()

    
    index_to_node = {idx: node for node, idx in mapping.items()}
    route_named = [index_to_node[idx] for idx in route]

    return route_named, distances[end_index]

if __name__ == '__main__':
    
    matrix, mapping = build_adjacency_matrix(nodes, graph_edges)
    print("Available Nodes:", nodes)
    
    source = input("Enter the source node: ").strip().upper()
    destination = input("Enter the destination node: ").strip().upper()

    if source not in mapping or destination not in mapping:
        print("Error: One or both of the nodes entered are invalid.")
        sys.exit(1)

    path, total_cost = dijkstra_shortest_route(matrix, mapping, source, destination)
    if total_cost == float('inf'):
        print(f"No valid route exists from {source} to {destination}.")
    else:
        print(f"Optimal path from {source} to {destination}: {' -> '.join(path)}")
        print(f"Total cost: {total_cost}")
