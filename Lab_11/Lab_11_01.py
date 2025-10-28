def create_adjacency_matrix():    
    input_str = input("Enter : ")
    edge_pairs = [edge.strip() for edge in input_str.split(',') if edge.strip()]
        
    nodes = set()
    edges = []

    for pair in edge_pairs:
        parts = pair.split()
        if len(parts) == 2:
            u, v = parts
            nodes.add(u)
            nodes.add(v)
            edges.append((u, v))

    sorted_nodes = sorted(list(nodes))
    num_nodes = len(sorted_nodes)
    
    node_to_index = {node: i for i, node in enumerate(sorted_nodes)}
    adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for u, v in edges:
        row_index = node_to_index[u]
        col_index = node_to_index[v]
        adj_matrix[row_index][col_index] = 1

    header = "    " + "  ".join(sorted_nodes)
    print(header)

    for i in range(num_nodes):
        row_node = sorted_nodes[i]
        row_str = ", ".join(map(str, adj_matrix[i]))
        print(f"{row_node} : {row_str}")

create_adjacency_matrix()