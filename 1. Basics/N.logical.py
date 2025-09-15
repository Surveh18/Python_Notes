"""
Logical Operators (Combining 2 or more than 2 conditional statements)

AND
C1   C2  Result
F    F   F
F    T   F
T    F   F
T    T   T

OR
C1   C2  Result
F    F   F
F    T   T
T    F   T
T    T   T

NOT - It reverese the result 
Result  Final_result(after applying NOT)
T       F
F       T

C1,C2 - Condition
"""

phy = 98
chem = 56

print(phy > 33 or chem > 33)




