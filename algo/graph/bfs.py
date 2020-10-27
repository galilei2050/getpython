from collections import deque
from util import read_graph


def dfs(graph):
    visited = set()
    discovered = dict()
    queue = deque()
    print('Traversal started')

    for vertice in graph.keys():
        if vertice in visited:
            continue
        queue.append(vertice)
        discovered[vertice] = None
        while queue:
            for i in range(len(queue)):
                current_vertice = queue.popleft()
                if current_vertice in visited:
                    continue
                visited.add(current_vertice)

                already_visited = len(visited)
                print(f"{already_visited} visit {current_vertice}")
                next_vertices = [
                    vertice for vertice in graph[current_vertice] if vertice not in visited]
                queue.extend(next_vertices)
                for next_vertice in next_vertices:
                    discovered[next_vertice] = current_vertice

    print('Traversal finished')
    return discovered


def main():
    graph = read_graph('aero.yml')
    discovered = dfs(graph)

if __name__ == "__main__":
    main()
