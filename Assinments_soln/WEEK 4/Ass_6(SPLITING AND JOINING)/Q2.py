"""
Q2. Write a function which accepts a String as a parameter and return the list of words.

my_string = "python is good"
w = words(my_string)
print(w)

# Output
['python','is','good']
"""


def words(s: str) -> list:
    return s.split()


print(words("  python   is   good  "))
# ['python', 'is', 'good']
