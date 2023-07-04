import networkx as nx
import matplotlib.pyplot as plt

def bellman_ford(graph, source):
    distance = {}
    predecessor = {}

    # Inicializar distancias y predecesores
    for node in graph.nodes:
        distance[node] = float('inf')
        predecessor[node] = None
    distance[source] = 0

    # Relajación de aristas repetidas
    for _ in range(len(graph.nodes) - 1):
        for u, v in graph.edges:
            weight = graph[u][v]['weight']
            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                predecessor[v] = u

    # Verificar existencia de ciclos negativos
    for u, v in graph.edges:
        weight = graph[u][v]['weight']
        if distance[u] + weight < distance[v]:
            raise ValueError("El grafo contiene un ciclo negativo")

    return distance, predecessor


# Crear el grafo
G = nx.DiGraph()
G.add_edge('Huánuco', 'Tingo María', weight=190)
G.add_edge('Tingo María', 'La Merced', weight=240)
G.add_edge('La Merced', 'San Ramón', weight=40)
G.add_edge('San Ramón', 'Chanchamayo', weight=45)
G.add_edge('Chanchamayo', 'La Oroya', weight=230)
G.add_edge('Huánuco', 'Cerro de Pasco', weight=190)
G.add_edge('Cerro de Pasco', 'La Oroya', weight=170)
G.add_edge('Tingo María', 'Yanayacu', weight=260)
G.add_edge('Yanayacu', 'Huancayo', weight=190)
G.add_edge('Huancayo', 'La Oroya', weight=125)
G.add_edge('Cerro de Pasco', 'La Merced', weight=220)
G.add_edge('Huancayo', 'Huancaya', weight=140)
G.add_edge('La Oroya', 'San Mateo', weight=80)
G.add_edge('Huancaya', 'Lima', weight=320)
G.add_edge('San Mateo', 'Lima', weight=100)
G.add_edge('Yanayacu', 'La Merced', weight=240)
G.add_edge('Huánuco', 'Yanahuanca', weight=80)
G.add_edge('Yanahuanca', 'Oyon', weight=80)
G.add_edge('Cerro de Pasco', 'Oyon', weight=100)
G.add_edge('Huaral', 'Lima', weight=75)
G.add_edge('Huánuco', 'San Miguel', weight=85)
G.add_edge('San Miguel', 'Oyon', weight=105)
G.add_edge('Cerro de Pasco', 'Huallay', weight=50)
G.add_edge('Huallay', 'Canta', weight=95)
G.add_edge('Canta', 'Lima', weight=100)
G.add_edge('Huallay', 'Huaral', weight=150)
G.add_edge('Oyon', 'Churin', weight=30)
G.add_edge('Churin', 'Sayán', weight=60)
G.add_edge('Sayán', 'Huaral', weight=60)

source_node = 'Huánuco'
target_node = 'Lima'

# Calcular el camino más corto
distance, predecessor = bellman_ford(G, source_node)

# Construir el camino desde el predecesor
path = [target_node]
while path[-1] != source_node:
    path.append(predecessor[path[-1]])
path.reverse()

# Calcular la longitud total del camino
length = distance[target_node]

print("Camino más corto:", path)
print("Longitud del camino más corto:", length)

# Definir las posiciones de los nodos manualmente
pos = {
    'Huánuco': (5, 5),
    'Tingo María': (6, 6),
    'La Merced': (5, 3.5),
    'San Ramón': (4.5, 3),
    'Chanchamayo': (3.5, 2.5),
    'La Oroya': (1.5, 1.5),
    'Cerro de Pasco': (3, 4),
    'Yanayacu': (6, 3),
    'Huancayo': (4.5, 2),
    'Lima': (0, 0),
    'Huancaya': (3, 0.5),
    'San Mateo': (1, 1),
    'Yanahuanca': (4, 5),
    'Oyon': (2, 5.5),
    'Huaral': (1, 2),
    'San Miguel': (3, 6),
    'Huallay': (3, 3),
    'Canta': (2.5, 1),
    'Churin': (1.7, 5),
    'Sayán': (1.3, 3.5)
}

# Crear una lista de colores para los nodos
node_colors = ['lightblue' for _ in G.nodes]

# Marcar los nodos de la ruta más corta en rojo
for i in range(len(path) - 1):
    u = path[i]
    v = path[i+1]
    G[u][v]['color'] = 'red'
    node_colors[list(G.nodes).index(u)] = 'red'
    node_colors[list(G.nodes).index(v)] = 'red'

# Visualizar el grafo de conexiones de vuelos con posiciones específicas
nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=[G[u][v].get('color', 'black') for u, v in G.edges])
edge_labels = nx.get_edge_attributes(G, 'weight')

# Mostrar etiquetas de peso en las aristas
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostrar resultado numérico en el gráfico
plt.text(0, 6.3, f"Camino más corto: {path}", fontsize=12, bbox=dict(facecolor='lightgray', edgecolor='black', boxstyle='round,pad=0.5'))
plt.text(0, 6, f"Longitud del camino más corto: {length}", fontsize=12, bbox=dict(facecolor='lightgray', edgecolor='black', boxstyle='round,pad=0.5'))

plt.show()
