import networkx as nx
from itertools import combinations

def is_dominating_set(G, nodes):
    dominated = set(nodes)
    for node in nodes:
        dominated.update(G.neighbors(node))
    return len(dominated) == len(G.nodes)

def find_min_dominating_set(G):
    for r in range(1, len(G.nodes) + 1):
        for subset in combinations(G.nodes, r):
            if is_dominating_set(G, subset):
                return set(subset)
    return set()

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])
    dom_set = find_min_dominating_set(G)
    print("Минимальное доминирующее множество:", dom_set)
