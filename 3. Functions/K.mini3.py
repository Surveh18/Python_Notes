"""
Create a function takes 3 integer as an argument 
Return the smallest number.

"""


def mini(a: int, b: int, c: int) -> int:
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    return c


print(mini(4, 22, 9))

# min is an inbuit function use to return the minimun value as well as same for max.


def find_minimum(a: int, b: int, c: int) -> int:
    x = min(a, b, c)  # applying min function here will return the min value from a,b,c.
    return x


print(find_minimum(4, 22, 9))  # Same output as above.


# when we hover the cursor on funcction we can see the definition of that function.
# we can change it according to us using doc strings.
# What ever we will write in docstrings it will reflect that line while doing hover on that cursor.
