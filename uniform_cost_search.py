# uniform_cost_search.py

import heapq

from graph_representation import graph
from constraint_satisfaction import is_safe, crowded_zones

def uniform_cost_search(start, goal):

    queue = [(0, start, [start])]
    visited = set()

    while queue:

        cost, current, path = heapq.heappop(queue)

        if current == goal:
            return path, cost

        if current not in visited:

            visited.add(current)

            for neighbor, edge_cost in graph[current].items():

                if is_safe(neighbor):

                    penalty = 5 if neighbor in crowded_zones else 0

                    heapq.heappush(
                        queue,
                        (
                            cost + edge_cost + penalty,
                            neighbor,
                            path + [neighbor]
                        )
                    )

    return None, float("inf")