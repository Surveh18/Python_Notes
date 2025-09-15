"""
Q7. Make two lists of same length and pass it to a function. Return a third
list where each element is the sum of index.


lst1 = [10, 25, 30, -10, 1, 9]
lst2 = [58, 11, -15, 20, 6, 1]
result = addition(lst1, lst2)
print(result)
# Output
[68, 36, 15, 10, 7, 10]
"""

result = []
lst1 = [10, 25, 30, -10, 1, 9]
lst2 = [58, 11, -15, 20, 6, 1]
for i in range(0, len(lst1)):
    result.append(lst1[i] + lst2[i])
print(result)
