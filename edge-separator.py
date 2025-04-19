import networkx as nx
from itertools import combinations

def is_disconnected_after_edge_removal(G, edges_to_remove):
    G_copy = G.copy()
    G_copy.remove_edges_from(edges_to_remove)
    return not nx.is_connected(G_copy)

def find_min_vertex_separator(G):
    edges = list(G.edges)
    answer = -1
    result = set()
    for r in range(1, len(edges) + 1):
        for edges_subset in combinations(edges, r):
            if is_disconnected_after_edge_removal(G, edges_subset) and (len(edges_subset) < answer or answer == -1):
                result = set(edges_subset)
                answer = r
    return answer, result

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])
    
    cnt, res = find_min_vertex_separator(G)
    print("Минимальное множество ребер для разрезания графа:", cnt)
    print("Ребра:", res)
