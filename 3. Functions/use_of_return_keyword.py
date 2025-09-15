# WITH RETURN KEYWORD
def Calc_sum(a, b):
    sum = a + b
    print(sum)  # Displays the result
    return sum  # Gives the result back to the program


result = Calc_sum(5, 2)  # `calc_sum` returns 7, and it gets stored in `result`
print("Result:", result)  # Prints "Result: 7"

# You can reuse `result`
another_calc = result + 10
print("Another Calculation:", another_calc)  # Prints "Another Calculation: 17"
"""
What happens here?
The function calculates the sum (5 + 2 = 7).
It prints 7.
It returns 7, which is stored in the variable result.
You can now use result for further calculations (e.g., result + 10).
"""


def calc_sum(a, b):  # Step 1: Define the function
    sum = a + b  # Step 2: Calculate sum
    print(sum)  # Step 3: Print the sum (side effect)
    return sum  # Step 4: Send the sum back to where the function was called


result = calc_sum(
    5, 2
)  # Step 5: Call the function and store its return value in `result`
print("Result:", result)  # Step 6: Use the returned value stored in `result`
