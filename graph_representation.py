# graph_representation.py

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 3, 'E': 5},
    'C': {'A': 4, 'F': 2},
    'D': {'B': 3, 'G': 4},
    'E': {'B': 5, 'G': 2},
    'F': {'C': 2, 'G': 3},
    'G': {'D': 4, 'E': 2, 'F': 3, 'EXIT': 1},
    'EXIT': {}
}

heuristic = {
    'A': 7,
    'B': 5,
    'C': 5,
    'D': 3,
    'E': 3,
    'F': 2,
    'G': 1,
    'EXIT': 0
}