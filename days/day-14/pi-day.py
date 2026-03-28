import math

def cut_pie(diameter: float, friends: int) -> float:
    if friends <= 0:
        raise ValueError("Number of friends must be greater than 0")

    circumference = math.pi * diameter
    crust_per_friend = circumference / friends

    return round(crust_per_friend, 2)