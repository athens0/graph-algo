import networkx as nx

def find_min_edge_cover(G):
    return nx.algorithms.covering.min_edge_cover(G)

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])
    edge_cover = find_min_edge_cover(G)
    print("Минимальное покрывающее множество рёбер:", edge_cover)
