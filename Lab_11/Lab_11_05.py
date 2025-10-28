def dijkstra_shortest_path():
    graph = {
        'A': {'B': 1, 'C': 2},
        'B': {'D': 12, 'A': 1},
        'C': {'D': 9, 'F': 3, 'A': 2},
        'D': {'C': 9, 'E': 7, 'G': 1},
        'E': {'G': 5, 'D': 7},
        'F': {'G': 4},
        'G': {'D': 1, 'E': 5, 'F': 4}
    }

    print(" *** Dijkstra's shortest path ***")

    start_vertex, target_vertex = input("Enter start and target vertex : ").split()


    if start_vertex not in graph or target_vertex not in graph:
        print(f"Error: Vertex not found in graph. Please choose from {list(graph.keys())}")
        return

    distances = {vertex: float('inf') for vertex in graph}
    predecessors = {vertex: None for vertex in graph}
    unvisited_nodes = set(graph.keys())
    
    distances[start_vertex] = 0

    while unvisited_nodes:
        current_vertex = None
        for vertex in unvisited_nodes:
            if current_vertex is None or distances[vertex] < distances[current_vertex]:
                current_vertex = vertex
        
        if distances[current_vertex] == float('inf'):
            break

        if current_vertex == target_vertex:
            break

        for neighbor, weight in graph[current_vertex].items():
            new_distance = distances[current_vertex] + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
        
        unvisited_nodes.remove(current_vertex)

    path = []
    current = target_vertex
    if distances[current] != float('inf'):
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]

    if not path or path[0] != start_vertex:
        print(f"No path found from {start_vertex} to {target_vertex}")
    else:
        print(f"Shortest distance is {distances[target_vertex]}")
        print(f"And the path is {path}")

dijkstra_shortest_path()