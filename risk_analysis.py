# risk_analysis.py

smoke_probability = {
    'A': 0.10,
    'B': 0.20,
    'C': 0.35,
    'D': 0.65,
    'E': 0.90,
    'F': 0.80,
    'G': 0.25,
    'EXIT': 0.00
}

def risk_level(probability):

    if probability >= 0.80:
        return "HIGH RISK"

    elif probability >= 0.50:
        return "MEDIUM RISK"

    else:
        return "LOW RISK"

def route_risk(path):

    total = 0

    for room in path:
        total += smoke_probability.get(room, 0)

    return total / len(path)