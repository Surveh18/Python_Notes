a = "Hello world"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
# space bhi ek character hai but space ko speacial treat mt krna
"""
H
e
l
l
o

w
"""

# iteration via index
for i in range(0, len(a)):
    print(a[i], end=" ")
# H e l l o   w o r l d

# iteration via value
for ch in a:
    print(ch, end=" ")
# H e l l o   w o r l d

# in reverse
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
# d l r o w   o l l e H
