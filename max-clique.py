import networkx as nx

def find_max_clique(G):
    return nx.approximation.max_clique(G)

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])

    clique = find_max_clique(G)
    print("Максимальная клика:", clique)
