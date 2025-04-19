import networkx as nx
from itertools import permutations

def hamiltonian_cycle(G):
    nodes = list(G.nodes)
    n = len(nodes)

    for perm in permutations(nodes):
        is_cycle = True
        for i in range(n):
            if not G.has_edge(perm[i], perm[(i + 1) % n]):
                is_cycle = False
                break
        if is_cycle:
            return perm + (perm[0],)
    return None

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (0, 1), (1, 2), (2, 3), (3, 0),
        (0, 2), (1, 3)
    ])

    cycle = hamiltonian_cycle(G)
    print("Гамильтонов цикл:", cycle if cycle else "не найден")
