import networkx as nx

def euler_info(G):
    has_eulerian_circuit = nx.is_eulerian(G)
    has_eulerian_path = nx.has_eulerian_path(G)

    circuit = list(nx.eulerian_circuit(G)) if has_eulerian_circuit else None
    path = list(nx.eulerian_path(G)) if has_eulerian_path else None

    return has_eulerian_path, has_eulerian_circuit, path, circuit

if __name__ == "__main__":
    G = nx.Graph()
    G.add_edges_from([
        (1, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 1)
    ])

    has_path, has_circuit, path, circuit = euler_info(G)
    print("Эйлеров путь существует:", has_path)
    print("Эйлеров цикл существует:", has_circuit)
    print("Путь:", path)
    print("Цикл:", circuit)
