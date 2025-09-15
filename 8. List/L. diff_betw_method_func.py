"""
-> difference between method and functions.
A **method** belongs to a specific data type and is called using dot (`.`) notation, like `list.append(4)`.  
A **function** is general and works on multiple data types, like `len(list)`. 

A method is called on an object of a specific type:
my_list = [1, 2, 3]
my_list.append(4)  # ✅ Works because append() is a method of list
print(my_list)  # Output: [1, 2, 3, 4]

If we try to call .append() on something thars not a list, it will give an error:
my_tuple = (1, 2, 3)
my_tuple.append(4)  # ❌ Error! Tuples don’t have append() method

A function like len() works on different data types:
print(len([1, 2, 3]))  # ✅ Works with list -> Output: 3
print(len("Hello"))  # ✅ Works with string -> Output: 5
print(len({1, 2, 3, 4}))  # ✅ Works with set -> Output: 4

"""
