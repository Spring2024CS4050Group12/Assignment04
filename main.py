import sys

from min_heap import MinHeap


def read_graph(file):
    n_vertices = int(file.readline())
    adjacency_list = [[] for i in range(n_vertices)]
    for line in file:
        s, e, w = line.split()
        start = int(s)
        end = int(e)
        weight = float(w)
        adjacency_list[start - 1].append((end, weight))
    
    return adjacency_list

def get_mst():
    pass

def main():
    with open('graph') as f:
        graph = read_graph(f)
    
    print(graph)

if __name__ == '__main__':
    main()