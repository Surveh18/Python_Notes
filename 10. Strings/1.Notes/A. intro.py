# immutable it cant be change
a = "Hello world"
print(type(a), a)
# <class 'str'> Hello world

# proof it is immutable it cant be change
a[2] = "Z"
print(a)
# TypeError: 'str' object does not support item assignment
