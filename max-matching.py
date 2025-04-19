import networkx as nx

def find_maximum_matching(G):
    matching = nx.algorithms.matching.max_weight_matching(G, maxcardinality=True)
    return matching

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])

    matching = find_maximum_matching(G)
    print("Максимальный Matching:", matching)
