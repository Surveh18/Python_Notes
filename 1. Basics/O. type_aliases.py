"""
-- Type Aliases in Python (Type Hints/Annotations).
let say hum koi jagah ek custom annotation use kr rhe hai
for example ek tuple hai jo float n float accept krti hai
tuple[float, float]
to iska naam do and iska shortcut bnado

Synatax:
type AliasName = SomeType
"""

type Point = tuple[float, float]


def distance(p1: Point, p2: Point) -> float:
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


p1: Point = (0.0, 0.0)
p2: Point = (3.0, 4.0)

print(distance(p1, p2))  # Output: 5.0

"""
ye point naam k shortcut ko dusri files mai bhi use kr skte hai

from file_path.file_name import Point
Ye syntax hai filhal work nhi krega q ki numbering di hai folders ko
"""
