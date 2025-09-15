# Parameters and Arguments
def addition():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(f"Total = {a+b}")


addition()


# In below line a,b variable is pass as parameters which is inside the function.
def sub(a, b):
    sub = a - b
    print(sub)


# here 100 & 33 is passed as arguments
sub(100, 33)

# NOTE : if we pass more than required argument or less than required arguments
# then it will be considered as typeerror.
# here it is not mention for sub which datatype we can use.
# Hover the cursor it will show unknown(datatype).

# here comes the annotation part.


def multiply(a: int, b: int, c: str | int):
    total = a * b * c
    print(total)


# here c variable can take str or int as a argument.
# this thing only works above py 3.9.1 version.

multiply(3, 4, 4)


def add(a: int, b: int):
    a = 12
    b = 10
    total = a + b
    print(total)


# In above function 1st we are taking user-input then after declaring
# a = 12 & b = 10 we are overwriting it dosen't make any sense.
# output will be always 22.
