def build_graph(edges_input):
    graph = {}
    
    edges = [e.strip().split() for e in edges_input.split(',') if e.strip()]
    
    def add_edge(u, v):
        if u not in graph:
            graph[u] = []
        if v not in graph[u]:
            graph[u].append(v)
            
    for u, v in edges:
        add_edge(u, v)
        add_edge(v, u)

    for node in graph:
        graph[node].sort()
        
    return graph

def find_all_vertices(graph):
    all_vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor in neighbors:
            all_vertices.add(neighbor)
            
    return sorted(list(all_vertices))

def depth_first_traversal_component(graph, start_node, visited):
    traversal_path = []
    stack = [start_node] 
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            traversal_path.append(node)

            neighbors = graph.get(node, [])
            reversed_neighbors = neighbors[::-1] 
            
            for neighbor in reversed_neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return traversal_path

def breadth_first_traversal_component(graph, start_node, visited):
    traversal_path = []
    queue = [start_node] 
    visited.add(start_node)
    
    while queue:
        node = queue.pop(0)
        traversal_path.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_path

def full_depth_first_traversal(graph):
    all_vertices = find_all_vertices(graph)
    visited = set()
    full_path = []
    
    for start_node in all_vertices:
        if start_node not in visited:
            component_path = depth_first_traversal_component(graph, start_node, visited)
            full_path.extend(component_path)
            
    return " ".join(full_path)

def full_breadth_first_traversal(graph):
    all_vertices = find_all_vertices(graph)
    visited = set()
    full_path = []
    
    for start_node in all_vertices:
        if start_node not in visited:
            # เริ่ม Traversal Component ใหม่
            component_path = breadth_first_traversal_component(graph, start_node, visited)
            full_path.extend(component_path)
            
    return " ".join(full_path)

def graph_traversals(input_edges_str):

    graph = build_graph(input_edges_str)
    
    dft_path = full_depth_first_traversal(graph)
    
    bft_path = full_breadth_first_traversal(graph)
    
    print(f"Depth First Traversals : {dft_path}")
    print(f"Bredth First Traversals : {bft_path}")

test_input_1 = input("Enter : ")
graph_traversals(test_input_1)