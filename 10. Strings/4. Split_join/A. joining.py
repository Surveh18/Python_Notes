"""
Joining - List (->) str

The .join() method in Python is used to combine elements of an iterable (like a list or tuple) into a single string.

It places the string (on which join() is called) between each element of the iterable.
"""

a = ["Surve", "h", "18"]
result1 = "".join(a)
result2 = " ".join(a)
result3 = " | ".join(a)
result4 = " ".join(i + "z" for i in a)
#         ↑
#       no-space & join k andr usko chaiye ek iterable which is a.
print(result1)  # Surveh18
print(result2)  # Surve h 18
print(result3)  # Surve | h | 18
print(result4)  # Survez hz 18z

"""
# Manual version of join
n = ["Surve", "h", "18"]
total = ""
for ch in n:
    total += ch
print(total)  # Surveh18

"""
"""
# using list comprehension
j = "a", "xyz", "586", "pqr"
final = "".join(i for i in j)
print(final)  # axyz586pqr
"""

"""
v = ["hey", "rollno", 21]
# result_v = " ".join(i for i in v)
# TypeError: sequence item 2: expected str instance, int found
result_v = " ".join(str(i) for i in v)
# incase koi int,float different datatype aajaye uske liye
print(result_v)  # hey rollno 21
"""
