import networkx as nx
from itertools import combinations

def is_vertex_cover(G, nodes):
    covered_edges = set()
    for u in nodes:
        for v in G.neighbors(u):
            covered_edges.add(frozenset((u, v)))
    return len(covered_edges) == len(G.edges)

def find_min_vertex_cover(G):
    for r in range(1, len(G.nodes) + 1):
        for subset in combinations(G.nodes, r):
            if is_vertex_cover(G, subset):
                return set(subset)
    return set()

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])
    vertex_cover = find_min_vertex_cover(G)
    print("Минимальное покрывающее множество вершин:", vertex_cover)
