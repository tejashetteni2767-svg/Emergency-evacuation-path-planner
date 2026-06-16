# depth_first_search.py

from graph_representation import graph
from constraint_satisfaction import is_safe

def depth_first_search(start, goal):

    stack = [(start, [start])]
    visited = set()

    while stack:

        current, path = stack.pop()

        if current == goal:
            return path

        if current not in visited:

            visited.add(current)

            for neighbor in graph[current]:

                if neighbor not in visited and is_safe(neighbor):
                    stack.append((neighbor, path + [neighbor]))

    return None