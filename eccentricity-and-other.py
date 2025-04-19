import networkx as nx

def graph_properties(G):
    ecc = nx.eccentricity(G)
    radius = nx.radius(G)
    diameter = nx.diameter(G)
    center = nx.center(G)
    
    return ecc, radius, diameter, center

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])

    ecc, radius, diameter, center = graph_properties(G)

    print("Эксцентриситет вершин:")
    for node, e in ecc.items():
        print(f"Вершина {node}: {e}")
    
    print("\nРадиус графа:", radius)
    print("Диаметр графа:", diameter)
    print("Центр графа:", center)
