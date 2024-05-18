import networkx as nx
import numpy as np

def leer_grafo(archivo):
    G = nx.DiGraph()
    with open(archivo, 'r') as file:
        for i, line in enumerate(file):
            for j, time_str in enumerate(line.strip()):
                if time_str != '0':
                    G.add_edge(chr(65 + i), chr(65 + j), time=int(time_str))
    return G

def floyd_warshall(grafo):
    nodes = sorted(grafo.nodes())
    n = len(nodes)
    dist_matrix = np.full((n, n), np.inf)
    path_matrix = np.full((n, n), -1)

    for i, u in enumerate(nodes):
        dist_matrix[i, i] = 0

    for u, v, data in grafo.edges(data=True):
        dist_matrix[nodes.index(u), nodes.index(v)] = data['time']
        path_matrix[nodes.index(u), nodes.index(v)] = nodes.index(v)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_matrix[i, k] + dist_matrix[k, j] < dist_matrix[i, j]:
                    dist_matrix[i, j] = dist_matrix[i, k] + dist_matrix[k, j]
                    path_matrix[i, j] = path_matrix[i, k]

    return dist_matrix, path_matrix

def obtener_camino_mas_corto(path_matrix, origen, destino):
    if np.isinf(path_matrix[origen, destino]):
        return None

    path = [origen]
    while path[-1] != destino:
        path.append(int(path_matrix[path[-1], destino]))
    return path

def letra():
    while True:
        letra_O = input("Ingresa el Orígen (A-J): ").upper()
        letra_D = input("Ingresa el Destino (A-J): ").upper()
        if letra_O in 'ABCDEFGHIJ' and letra_D in 'ABCDEFGHIJ':
            return letra_O, letra_D
        else:
            print("La letra ingresada de orígen/destino no es válida.")

G = leer_grafo("C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 3/UNITY/Python/matriz_tiempos.txt")

dist_matrix, path_matrix = floyd_warshall(G)

letra_origen, letra_destino = letra()
origen = sorted(G.nodes()).index(letra_origen)
destino = sorted(G.nodes()).index(letra_destino)

camino_mas_corto = obtener_camino_mas_corto(path_matrix, origen, destino)

def guardar_camino_txt(camino_mas_corto_letras):
    ruta_py = "C:camino.txt"
    ruta_unity= "C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 3/UNITY/Python/camino.txt"

    with open(ruta_py, 'w') as file1, open(ruta_unity, 'w') as file2:
        if camino_mas_corto_letras:
            for letra in camino_mas_corto_letras:
                file1.write(letra + "\n")
                file2.write(letra + "\n")
        else:
            file1.write("No hay un camino disponible")
            file2.write("No hay un camino disponible")

if camino_mas_corto:
    camino_mas_corto_letras = [sorted(G.nodes())[i] for i in camino_mas_corto]
    print("El camino más corto de", letra_origen, "a", letra_destino, "es:", camino_mas_corto_letras)
    guardar_camino_txt(camino_mas_corto_letras)
else:
    print("No hay un camino disponible entre", letra_origen, "y", letra_destino)
