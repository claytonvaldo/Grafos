import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, vertices, arestas, direcionado=True, ponderado=True):
        self.vertices = vertices
        self.arestas = arestas
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.adjacencia = {v: [] for v in vertices}
        self.umGrafo = nx.DiGraph() if direcionado else nx.Graph()
        self.construirGrafo()

    def construirGrafo(self):
        self.umGrafo.add_nodes_from(self.vertices)
        for a in self.arestas:
            partes = a.split("-")
            u, v = partes[0], partes[1]
            peso = int(partes[2]) if self.ponderado and len(partes) == 3 else 1
            self.umGrafo.add_edge(u, v, weight=peso)
            self.adjacencia[u].append((v, peso))
            if not self.direcionado:
                self.adjacencia[v].append((u, peso))

    def exibirAdjacencia(self):
        print("Lista de adjacência:")
        for v, vizinhos in self.adjacencia.items():
            print(f"{v}: {vizinhos}")

    def desenhar(self):
        pos = nx.spring_layout(self.umGrafo)
        plt.figure(figsize=(6, 5))
        nx.draw(self.umGrafo, pos, with_labels=True, node_color='lightblue',
                node_size=2000, font_size=10, arrows=self.direcionado)
        if self.ponderado:
            labels = nx.get_edge_attributes(self.umGrafo, 'weight')
            nx.draw_networkx_edge_labels(self.umGrafo, pos, edge_labels=labels)
        plt.title("Grafo Gerado")
        plt.axis('off')  # Remove eixos
        plt.show()

# Dados de entrada
listaVertices = ['A', 'B', 'C', 'D', 'E']
listaArestas = ['A-B-4', 'B-C-5', 'C-D-1', 'D-A-2', 'E-A-3']
direcionado = True
ponderado = True

# Instancia e executa
meuGrafo = Grafo(listaVertices, listaArestas, direcionado, ponderado)
meuGrafo.exibirAdjacencia()
meuGrafo.desenhar()
