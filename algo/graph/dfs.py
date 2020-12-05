from yaml import load, dump
from collections import deque
from pathlib import Path


def dfs(graph, root_vertice=None):
    visited = set()
    discovered = dict()
    root_vertices = [root_vertice] if root_vertice else graph.keys()
    connected_components = []
    for vertice in root_vertices:
        if vertice in visited:
            continue
        connected_vertices = []
        discovered[vertice] = None
        stack = deque()
        stack.append(vertice)
        while stack:
            current_vertice = stack.pop()
            if current_vertice in visited:
                continue
            print(f"Visit {current_vertice}")
            visited.add(current_vertice)
            connected_vertices.append(current_vertice)
            next_vertices = [vertice for vertice in graph.get(current_vertice, []) if vertice not in visited]
            stack.extend(next_vertices)

            for next_vertice in next_vertices:
                discovered[next_vertice] = current_vertice
        connected_components.append(connected_vertices)
    for connected_component in connected_components:
        print("Component ", connected_component)

    return discovered


def get_path(source, destination, discovered):
    if destination not in discovered:
        return []

    path = [destination]
    current_vertice = destination
    while current_vertice != source and current_vertice is not None:
        current_vertice = discovered[current_vertice]
        path.append(current_vertice)

    return list(reversed(path))


def main():
    graph = load(Path('graph.yml').read_bytes())
    # source, destination = 'JFK', 'LAX'
    dfs(graph)
    # discovered = dfs(graph, root_vertice = source)
    # path = get_path(source, destination, discovered)
    # print(f'Path from {source} to {destination} is ', path)


if __name__ == '__main__':
    main()

