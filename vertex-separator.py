import networkx as nx
from itertools import combinations

def is_disconnected_after_removal(G, vertices_to_remove):
    G_copy = G.copy()
    G_copy.remove_nodes_from(vertices_to_remove)
    return not nx.is_connected(G_copy)

def find_min_vertex_separator(G):
    n = len(G.nodes)
    answer = -1
    result = set()
    for r in range(1, n):
        for nodes in combinations(G.nodes, r):
            if is_disconnected_after_removal(G, nodes) and (len(nodes) < answer or answer == -1):
                result = set(nodes)
                answer = r
    return answer, result

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])
    
    cnt, res = find_min_vertex_separator(G)
    print("Минимальное множество вершин для разрезания графа:", cnt)
    print("Вершины:", res)
