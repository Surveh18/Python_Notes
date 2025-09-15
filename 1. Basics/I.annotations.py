"""
Python is called a dynamically typed language

for example if i write person(variable_name) and assign
the value(surve) the assign 23 value to same variable
which is allowed in python and we can also called it
a part of dynamically_typed

Note - A single variable can change its data type where in c++,Java is not allowed.

To overcome this annotation is here.
"""

""" 
BEFORE USING ANNOTATIONS : 

name = "surve"
print(name)

name = 12
print(name)

name = True
print(name)

# Output
surve
12
True

"""

# AFTER APPLYING(USING) ANNOTATIONS :
# What we can do is declaring data_type with variable name
# which tells the interpreter that this variable(name) has only this data_type(str).

# name: str = "surve"
# print(name)

name = 765
# error in upper-line
print(name)

age: float = 88.99
age = -12
# age = "hello"
# error in upper-line(if remove comment)

# the code will still execute but an error will be pop-up.

name: str | int = "surve"
name = "harshal"
name = 89
# name =12.98
# error in upper-line(if remove comment)
