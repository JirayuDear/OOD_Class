def find_shortest_paths():

    input_str = input("Enter : ")
    graph_str, queries_str = input_str.split('/')

    graph = {}
    all_nodes = set()

    edges = [edge.strip() for edge in graph_str.split(',') if edge.strip()]
    for edge in edges:
        parts = edge.split()
        if len(parts) != 3:
            continue
        
        u, weight_str, v = parts
        try:
            weight = int(weight_str)
        except ValueError:
            continue
        
        all_nodes.add(u)
        all_nodes.add(v)
        
        if u not in graph:
            graph[u] = {}
        graph[u][v] = weight

    for node in all_nodes:
        if node not in graph:
            graph[node] = {}
            
    queries = [query.strip().split() for query in queries_str.split(',') if query.strip()]

    for query in queries:
        if len(query) != 2:
            continue
        start_node, end_node = query

        if start_node not in graph or end_node not in graph:
            print(f"Not have path : {start_node} to {end_node}")
            continue

        distances = {node: float('inf') for node in graph}
        predecessors = {node: None for node in graph}
        distances[start_node] = 0
        
        unvisited_nodes = set(graph.keys())

        while unvisited_nodes:
            min_distance_node = None
            for node in unvisited_nodes:
                if min_distance_node is None or distances[node] < distances[min_distance_node]:
                    min_distance_node = node

            if distances[min_distance_node] == float('inf'):
                break

            current_node = min_distance_node
            
            for neighbor, weight in graph[current_node].items():
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
            
            unvisited_nodes.remove(current_node)
        
        if distances[end_node] == float('inf'):
            print(f"Not have path : {start_node} to {end_node}")
        else:
            path = []
            current = end_node
            while current is not None:
                path.insert(0, current)
                current = predecessors[current]
            
            print(f"{start_node} to {end_node} : {'->'.join(path)}")

find_shortest_paths()