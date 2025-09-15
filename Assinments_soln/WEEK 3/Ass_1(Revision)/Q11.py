"""
Qll. Create a function that takes damage and speed (attacks per second)
and returns the amount of damage after a given time.

# Examples:
• damage(40, 5, "second") -> 200
• damage(1OO, 1, "minute") -> 6000
• damage(2, 100, "hour") -> 720000

Return "invalid" if damage or speed is negative-
"""


def damage(damage_per_attack: int, speed: int, time: str):
    if time == "second" or time == "Second":
        total_damage = damage_per_attack * speed * 1
    elif time == "minute" or time == "Minute":
        total_damage = damage_per_attack * speed * 60
    elif time == "hour" or time == "Hour":
        total_damage = damage_per_attack * speed * 3600
    return total_damage


print(damage(40, 5, "second"))
print(damage(100, 1, "minute"))
print(damage(2, 100, "hour"))
