a = (10, "surve", True, 11.43, 55.55)
print(a)  # (10, 'surve', True, 11.43, 55.55)
print(type(a))  # <class 'tuple'>

"""
# Tuple is immutable means na isme add krskte hai naa change
# Proof tuple is immutable
a[3] = 34
print(a)
# TypeError: 'tuple' object does not support item assignment
# Above i m trying the update the 3 index value which is not possible.
"""

# isme pop,remove jesa kuch bhi nhi hai.
# Tuple mai sirf 2 methods hote hai index,count
c = a.index(11.43)
print(c)
# Return first index of value.
# Raises ValueError if the value is not present.
