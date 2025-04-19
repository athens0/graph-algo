import networkx as nx
import matplotlib.pyplot as plt

vertices = []
for i in range(0, 4):
    for j in range(0, 6):
        vertices.append((i, j))

edges = []
for v in vertices:
    x, y = v
    edges.append(((x, y), (0, y)))
    edges.append(((x, y), (x, 0)))
    edges.append(((x, y), (3, y)))
    edges.append(((x, y), (x, 5)))
    to_left = min(3 - x, y)
    to_right = min(x, 5 - y)
    edges.append(((x, y), (x + to_left, y - to_left)))
    edges.append(((x, y), (x - to_right, y + to_right)))

new_edges = []
for i in range(len(edges)):
    e = edges[i]
    if e[0] == e[1]:
        continue
    if e[1] == (0, 0):
        continue
    new_edges.append(e)

G = nx.Graph()
G.add_edges_from(new_edges)

pos = nx.shell_layout(G)

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, edge_color='gray')
plt.show()
