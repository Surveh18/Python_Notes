"""
Q1. Given a list of strings, concatenate them into a single string separated
by spaces. For example, given the input ["Hello", "World", "Python"],
the output should be "Hello World Python".
Make a list on your own.
Don’t use the JOIN function.
"""

n = ["Hello", "World", "Python"]
new_list = str()
for i in n:
    new_list += i + " "
# last extra space hata do
new_list = new_list.strip()
print(str(new_list))
# Hello World Python
