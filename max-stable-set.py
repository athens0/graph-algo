import networkx as nx

def find_max_stable_set(G):
    complement = nx.complement(G)
    return nx.approximation.max_clique(complement)

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])

    indep = find_max_stable_set(G)
    print("Максимальный Stable set:", indep)
