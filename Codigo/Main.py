from view import visualizar_grafo_com_caminho


def is_safe(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True


def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        return True
    for v in range(1, len(graph)):
        if is_safe(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False


def hamiltonian_path(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not hamiltonian_util(graph, path, 1):
        print("Nenhum caminho Hamiltoniano encontrado.")
        return None
    print("Caminho Hamiltoniano encontrado:")
    print(path)
    return path


if __name__ == "__main__":
    graph = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 1, 0]
    ]
    caminho = hamiltonian_path(graph)
    visualizar_grafo_com_caminho(graph, caminho)
