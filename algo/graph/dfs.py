from collections import deque
from typing import Coroutine
from util import read_graph


def dfs(graph):
    visited = set()
    discovered = dict()
    stack = deque()
    print('Traversal started')

    for vertice in graph.keys():
        if vertice in visited:
            continue
        stack.append(vertice)
        discovered[vertice] = None
        while stack:
            current_vertice = stack.pop()
            if current_vertice in visited:
                continue
            visited.add(current_vertice) 

            already_visited = len(visited)
            print(f"{already_visited} visit {current_vertice}")
            next_vertices = [
                vertice for vertice in graph[current_vertice] if vertice not in visited]
            stack.extend(next_vertices)
            for next_vertice in next_vertices:
                discovered[next_vertice] = current_vertice

    print('Traversal finished')
    return discovered


def find_path(source, destination, discovered):
    if destination not in discovered:
        return []

    path = [destination]
    current_vertice = destination
    while current_vertice != source and current_vertice is not None:
        current_vertice = discovered.get(current_vertice, None)
        if current_vertice is None:
            return []
        path.append(current_vertice)
    return list(reversed(path))


def main():
    graph = read_graph('aero.yml')
    discovered = dfs(graph)
    path = find_path('BOS', 'ORD', discovered)
    print(f"Path BOS->ORD is {path}")
    for i, vertice in enumerate([k for k, v in discovered.items() if v is None]):
        print(f'{i} root is {vertice}')


if __name__ == "__main__":
    main()
