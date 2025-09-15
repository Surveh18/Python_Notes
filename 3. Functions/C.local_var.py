# Local variable and scope.
"""
scope - means upto where the variable will be valid to use.

local var means its scope will be or can be used only
in that function if we use it outside that function
it will show error.
"""


def add():
    # a, b, total are local_variable.
    a = 10
    b = 20
    total = a + b
    print(total)


add()

# print(a)
# now if i use a_var here as print(a) it will show Name_error
num = 100
# here num_variable is global variable.
