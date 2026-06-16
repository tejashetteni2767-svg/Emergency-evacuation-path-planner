# final_integration.py

from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search
from uniform_cost_search import uniform_cost_search
from a_star_search import a_star_search
from greedy_best_first_search import greedy_best_first_search

from risk_analysis import route_risk, risk_level
from decision_making import minimax_decision

print("=" * 50)
print("EMERGENCY EVACUATION PATH PLANNER")
print("=" * 50)

start_room = input("Enter Start Room (A-G): ").upper()
goal = "EXIT"

bfs_path = breadth_first_search(start_room, goal)
dfs_path = depth_first_search(start_room, goal)

ucs_path, ucs_cost = uniform_cost_search(start_room, goal)

astar_path, astar_cost = a_star_search(start_room, goal)

greedy_path = greedy_best_first_search(start_room, goal)

print("\n===== SEARCH RESULTS =====")

print("\nBreadth First Search")
print("Path:", bfs_path)

print("\nDepth First Search")
print("Path:", dfs_path)

print("\nUniform Cost Search")
print("Path:", ucs_path)
print("Cost:", ucs_cost)

print("\nA-Star Search")
print("Path:", astar_path)
print("Cost:", astar_cost)

print("\nGreedy Best First Search")
print("Path:", greedy_path)

if astar_path:

    risk = route_risk(astar_path)

    print("\n===== RISK ANALYSIS =====")

    print("Recommended Route:")
    print(" -> ".join(astar_path))

    print("Average Risk:")
    print(round(risk * 100, 2), "%")

    print("Risk Level:")
    print(risk_level(risk))

    print("\n===== DECISION =====")
    print(minimax_decision(risk))
