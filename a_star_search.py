# a_star_search.py

import heapq

from graph_representation import graph, heuristic
from constraint_satisfaction import is_safe, crowded_zones

def a_star_search(start, goal):

    queue = [(0, start, [start], 0)]
    visited = set()

    while queue:

        f_cost, current, path, g_cost = heapq.heappop(queue)

        if current == goal:
            return path, g_cost

        if current not in visited:

            visited.add(current)

            for neighbor, edge_cost in graph[current].items():

                if is_safe(neighbor):

                    penalty = 5 if neighbor in crowded_zones else 0

                    new_g = g_cost + edge_cost + penalty
                    new_f = new_g + heuristic[neighbor]

                    heapq.heappush(
                        queue,
                        (
                            new_f,
                            neighbor,
                            path + [neighbor],
                            new_g
                        )
                    )

    return None, float("inf")