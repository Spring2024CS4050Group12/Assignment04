from min_heap import MinHeap


def read_graph(file):
    n_vertices = int(file.readline())
    adjacency_list = [[] for i in range(n_vertices)]
    for line in file:
        s, d, w = line.split()
        source = int(s) - 1
        destination = int(d) - 1
        weight = float(w)
        adjacency_list[source].append((weight, destination))
        adjacency_list[destination].append((weight, source))
    
    return adjacency_list

def get_mst(graph):
    heap = MinHeap()
    tree = []  # list of edges
    total_weight = 0
    seen = {0}

    # start with vertex 0 per instructions
    for neighbor_weight, neighbor in graph[0]:
        heap.add(neighbor, (neighbor_weight, 0))

    while len(heap) > 0:
        destination, (weight, source) = heap.pop()
        tree.append((source, destination, weight))
        total_weight += weight
        seen.add(destination)

        for neighbor_weight, neighbor in graph[destination]:
            if neighbor in seen:
                continue

            # Note: The destination of the incoming edge is the source of the
            #  outgoing edge
            outgoing_edge = (neighbor_weight, destination)

            if neighbor in heap:
                heap.decrease_value(neighbor, outgoing_edge)
            else:
                heap.add(neighbor, outgoing_edge)
    
    return tree, total_weight

def main():
    with open('graph') as f:
        graph = read_graph(f)
    
    print("Finding an MST for the following graph:")
    for i, outgoing_edges in enumerate(graph):
        print(f"Vertex {i + 1} is adjacent to: {', '.join(f'{destination + 1} (weight: {weight})' for (weight, destination) in outgoing_edges)}")
    print()
    
    mst, total_weight = get_mst(graph)
    print("An MST for the graph above is as follows:")
    for source, destination, weight in mst:
        print(f"{source + 1} to {destination + 1} (weight {weight})")
    
    print(f"With a total cost of {total_weight}")

if __name__ == '__main__':
    main()
