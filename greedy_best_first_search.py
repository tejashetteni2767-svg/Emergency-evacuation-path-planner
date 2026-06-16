# greedy_best_first_search.py

import heapq

from graph_representation import graph, heuristic
from constraint_satisfaction import is_safe

def greedy_best_first_search(start, goal):

    queue = [(heuristic[start], start, [start])]
    visited = set()

    while queue:

        h, current, path = heapq.heappop(queue)

        if current == goal:
            return path

        if current not in visited:

            visited.add(current)

            for neighbor in graph[current]:

                if is_safe(neighbor):

                    heapq.heappush(
                        queue,
                        (
                            heuristic[neighbor],
                            neighbor,
                            path + [neighbor]
                        )
                    )

    return None