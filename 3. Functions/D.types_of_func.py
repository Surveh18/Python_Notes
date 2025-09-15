"""
4 types:

1.Without parameters, without Return
2.With parameters, without Return
3.Without parameters, with Return
4.With parameters, with Return

"""


# 1. Without parameters, without return.
# Function Declaration / Creation.
def greet():
    print("Hello user")


# function calling
greet()


# 2.With parameters, without return.
# Function Declaration.
# Here every-time we run this add function it needs 2 values(a,b) known as parameters.
def add(a, b):
    print(a + b)


add(5, 10)
# Here we are passing arguments 5,10 to add function.


# 3.Without parameters, with return.
def multiply_numbers():
    num1 = 6
    num2 = 4
    product = num1 * num2
    return product


# Call the function and use the returned value
result = multiply_numbers()
print(f"The product is: {result}")
"""
The multiply_number() function multiplies two fixed numbers(6*4) and 
returns result (24).

The returned value(24) is stored in result and then printed.

"""


# 4.With parameters, with return.
def add_numbers(num1, num2):
    result = num1 + num2
    return result


# Calling the function with arguments and capturing the return value
sum_result = add_numbers(10, 20)
print(f"The sum is: {sum_result}")
"""
The function add_numbers takes two parameters, num1, num2
which you need to provide when calling the function.

Inside the function, num1 and num2 are added together, and the result is returned.

The return value is stored in the variable sum_result, which is then printed.
"""
