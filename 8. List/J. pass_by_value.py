# Pass by value will work in -> int, floats,strings.
# Pass by value is immutable. The thing which cannot be change.
def change(a, b):
    # a,b local variables scope till its function
    a = 110
    b = 110


# Global variables.
a = 1
b = 1
change(a, b)  # Function call
print(a)  # This will print global variables.
print(b)
# Thus we are calling function but doing any print/return it will do nothing.
# Output - 1 1
"""
-> suppose i give my phone no. to the function it depends on it.
for what purpose it will use. On basis of its use there will be no changes made in my number.
"""
