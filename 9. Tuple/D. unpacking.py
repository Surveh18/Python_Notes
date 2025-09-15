a = 12, 45, 32, 11, 91, 90, 98
print(a)  # (12, 45, 32, 11, 91, 90, 98)
# aap (bracket) na lagao to bhi tuple create hoga

a1 = 12
print(type(a1), a1)  # <class 'int'> 12

# What if mujhe tuple mai sirf ek value store krni ho to vo lekin int mai consider hoga
# n agr mai a = (12) eese karu to formater brackets hta dega to sirf ek comma(,) add krna hai

b = (12,)
print(type(b), b)  # <class 'tuple'> (12,)

# UNPACKING CONCEPT:- jo bhi chizz iterable hai usse unpack kr skte hai

a, b, c = [1, 2, 3]
print(a, type(a))
print(b, type(b))
print(c, type(c))
"""
1 <class 'int'>
2 <class 'int'>
3 <class 'int'>
"""
x, y = 33, 6  # ye bhi basically tuple hi hai isko bhi unpack krte hai
print(x, type(x))
print(y, type(y))
"""
33 <class 'int'>
6 <class 'int'>
"""
