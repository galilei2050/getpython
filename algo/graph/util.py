from yaml import load
from pathlib import Path


def read_graph(file_path):
    graph = load(Path(file_path).read_bytes())
    return graph
