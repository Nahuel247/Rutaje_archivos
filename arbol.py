import os
import re
import networkx as nx
import matplotlib.pyplot as plt

def dibujar_grafo(grafo, layout_func):
    import matplotlib.pyplot as plt
    pos = layout_func(grafo)
    nx.draw(grafo, pos, with_labels=True, node_size=2000, font_size=12, font_weight='bold')
    plt.show()


def arbol(path):
    # Crear directorio si no existe
    if not os.path.exists('Arbol1'):
        os.makedirs('Arbol1')

    # Lista todos los archivos .py en el directorio
    archivos = [f for f in os.listdir(path) if f.endswith('.py')]

    # Crear matriz de adyacencia y grafo
    matriz = [[0]*len(archivos) for _ in archivos]
    grafo = nx.DiGraph()

    # Para cada archivo
    for i, archivo in enumerate(archivos):
        # Leer contenido del archivo
        with open(os.path.join(path, archivo)) as f:
            contenido = f.read()

        # Para cada archivo objetivo que no sea el mismo
        for j, objetivo in enumerate(archivos):
            if archivo != objetivo:
                # Verificar si el archivo objetivo es mencionado en el archivo
                if objetivo.replace('.py', '') in contenido:
                    # Actualizar matriz y grafo
                    matriz[i][j] = 1
                    grafo.add_edge(archivo, objetivo)

    # Guardar la matriz
    with open('Arbol1/matriz.txt', 'w') as f:
        for fila in matriz:
            f.write(' '.join(str(x) for x in fila) + '\n')

    # Dibujar el grafo
    dibujar_grafo(grafo, nx.spring_layout)
    plt.show()

path="ruta"
arbol("C:/Users/Asus/OneDrive/Proyectos/Rutaje_archivos/Proyecto")
