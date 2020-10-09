from yaml import load, dump
from collections import deque
from pathlib import Path

tree = load(Path('tree.yml').read_bytes())


class BinaryTreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []


def bfs(tree):
    queue = deque()
    queue.append(tree['root'])
    sum_of_levels = []
    while len(queue) > 0:
        sum_of_level = 0
        for i in range(len(queue)):
            node = queue.popleft()

            sum_of_level += node['value']
            print(f"visit {node['value']}")

            for child in ['left', 'right']:
                c = node.get(child, None)
                if c:
                    queue.append(c)
        sum_of_levels.append(sum_of_level)
        print('===========')
    print(sum_of_levels)


def dfs(tree):
    queue = deque()
    queue.append(tree['root'])
    while len(queue) > 0:
        node = queue.pop()
        print(f"visit {node['value']}")
        for child in ['right', 'left']:
            c = node.get(child, None)
            if c:
                queue.append(c)


def postorder(node):
    for child in ['right', 'left']:
        c = node.get(child, None)
        if c is not None:
            postorder(c)
    print(f"visit {node['value']}")


postorder(tree['root'])
