import matplotlib.pyplot as plt
import networkx as nx
import os
import matplotlib
matplotlib.use('Agg')  # Força backend sem interface gráfica (Tkinter)


def visualizar_grafo_com_caminho(graph, caminho, salvar_em='assets/grafo_hamiltoniano.png'):
    # Garante que a pasta exista
    os.makedirs(os.path.dirname(salvar_em) or '.', exist_ok=True)

    G = nx.Graph()

    for i in range(len(graph)):
        G.add_node(i)

    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    edge_colors = []
    caminho_arestas = set()

    if caminho:
        for i in range(len(caminho) - 1):
            aresta = (caminho[i], caminho[i + 1])
            caminho_arestas.add(aresta)
            caminho_arestas.add((aresta[1], aresta[0]))

    for u, v in G.edges():
        if (u, v) in caminho_arestas:
            edge_colors.append("red")
        else:
            edge_colors.append("gray")

    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G, pos, with_labels=True, node_color='skyblue',
        edge_color=edge_colors, node_size=800, font_weight='bold'
    )

    plt.title("Caminho Hamiltoniano")
    plt.savefig(salvar_em)
    plt.close()
    print(f"Imagem salva com sucesso em: {salvar_em}")
