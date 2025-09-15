from typing import Dict, List

details: Dict[str, List[int]] = {
    "Ani": [45, 44, 33, 12, 5, 6, 45, 6, 2],
    "sanjay": [67, 89, 96],
    "vandana": [76, 43, 53, 21, 22],
    "Vivek": [11, 22, 31, 78, 94],
}

"""
ani has scored 320 marks
sanjay has scored 210 marks
"""

for name, marks in details.items():
    total = int()
    for m in marks:
        total += m
    print(f"{name} has scored {total} marks.")
