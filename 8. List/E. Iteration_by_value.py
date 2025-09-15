# Iteration by value.
list = [12, 33, 76, 90, 0, -2, 4, -45]

for i in list:
    print(i, end=" ")

for index, value in enumerate(list):
    print(f"Value at {index} index is = {value}")
# enumerate means who gives index and value of an element.
