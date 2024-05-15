import networkx as nx
import numpy as np

G = nx.DiGraph()
def guardar_matriz_tiempo(matriz, filename):
    with open(filename, 'w') as file:
        for row in matriz:
            file.write(''.join(map(str, row)) + '\n')

nodo = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J'
}

G.add_nodes_from(nodo.values())

tiempo = [
    ('A', 'C', {'time': 3}),
    ('A', 'J', {'time': 9}),
    ('B', 'F', {'time': 7}),
    ('B', 'I', {'time': 4}),
    ('C', 'D', {'time': 2}),
    ('C', 'G', {'time': 6}),
    ('C', 'E', {'time': 8}),
    ('D', 'E', {'time': 1}),
    ('H', 'H', {'time': 5}),
    ('F', 'J', {'time': 9}),
    ('G', 'H', {'time': 3}),
    ('I', 'J', {'time': 7}),
    ('A', 'B', {'time': 5}),
    ('D', 'F', {'time': 4}),
    ('G', 'I', {'time': 2})
]

G.add_edges_from(tiempo)

ad_matriz = nx.to_numpy_array(G, nodelist=sorted(G.nodes()))
t_matriz = np.zeros(ad_matriz.shape, dtype=int)

for origen, destino, data in G.edges(data=True):
    origen_id = sorted(G.nodes()).index(origen)
    destino_id = sorted(G.nodes()).index(destino)
    t_matriz[origen_id, destino_id] = data['time']

print("Matriz de Adyacencia:")
print(ad_matriz)
print("\nMatriz de Tiempos:")
print(t_matriz)
guardar_matriz_tiempo(t_matriz, "matriz_tiempos.txt")

def guardar_txt(graph, filename):
    with open(filename, 'w') as file:
        file.write("Nodos con tiempos:\n")
        for edge in graph.edges(data=True):
            file.write(f"{edge[0]}, {edge[1]}, {edge[2]['time']}\n")
guardar_txt(G, "grafica.txt")