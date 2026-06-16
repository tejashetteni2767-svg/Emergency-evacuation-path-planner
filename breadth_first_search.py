# breadth_first_search.py

from collections import deque
from graph_representation import graph
from constraint_satisfaction import is_safe

def breadth_first_search(start, goal):

    queue = deque([(start, [start])])
    visited = set()

    while queue:

        current, path = queue.popleft()

        if current == goal:
            return path

        if current not in visited:

            visited.add(current)

            for neighbor in graph[current]:

                if neighbor not in visited and is_safe(neighbor):
                    queue.append((neighbor, path + [neighbor]))

    return None