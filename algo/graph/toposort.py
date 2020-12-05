from yaml import load, dump
from pathlib import Path
from collections import defaultdict


def topo(graph):
    visited = set()
    topologically_sorted = []
    for vertice in graph.keys():
        if vertice in visited:
            continue
        stack = [vertice]
        while stack:
            current_vertice = stack[-1]
            print('Visit', current_vertice)

            next_vertices = [v for v in graph.get(current_vertice, []) if v not in visited]
            if set(next_vertices) & set(stack):
                print('Cycle detected')
                return []
            if not next_vertices:
                print('Emit ', current_vertice)
                visited.add(current_vertice)
                topologically_sorted.append(current_vertice)
                stack.pop()
            else:
                stack.extend(next_vertices)

            # print('Visit', current_vertice)
            # visited.add(current_vertice)
            # stack.extend(graph.get(current_vertice, []))

    return topologically_sorted


def main():
    graph = load(Path('t.yml').read_bytes())
    print(topo(graph))


def alien_dict(words):
    # Step 0: Put all unique letters into the adj list.
    reverse_adj_list = {c : [] for word in words for c in word}

    # Step 1: Find all edges and put them in reverse_adj_list.
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                reverse_adj_list[d].append(c)
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word):
                return ""

    relations = defaultdict(set)
    for word1, word2 in zip(words[:-1], words[1:]):
        i = 0
        while i < min(len(word1), len(word2)) and word1[i] == word2[i]:
            i += 1
        if i == min(len(word1), len(word2)):
            continue
        relations[word2[i]].add(word1[i])
    print(relations)
    visited = set()
    sorted_letters = []

    for char in relations:
        if char in visited:
            continue
        stack = [char]
        while stack:
            current_char = stack[-1]
            next_letters = [ch for ch in relations.get(current_char, []) if ch not in visited]
            if set(stack) & set(next_letters):
                print('cycle', current_char, stack, next_letters)
                return []
            if not next_letters:
                visited.add(current_char)
                sorted_letters.append(current_char)
                stack.pop()
            else:
                stack.extend(next_letters)
    print(sorted_letters)
    return  sorted_letters


if __name__ == '__main__':
    alien_dict(
        [
            'z',
            "z",
        ]
    )
