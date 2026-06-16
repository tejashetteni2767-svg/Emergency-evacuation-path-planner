# constraint_satisfaction.py

fire_zones = ['E']
smoke_zones = ['F']
crowded_zones = ['D']

def is_safe(room):
    return room not in fire_zones and room not in smoke_zones