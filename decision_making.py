# decision_making.py

def minimax_decision(risk):

    if risk >= 0.60:
        return "SWITCH TO SAFER ROUTE"

    return "KEEP CURRENT ROUTE"