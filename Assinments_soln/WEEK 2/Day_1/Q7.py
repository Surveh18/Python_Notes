"""
Q7. Write a function named celsius_to_fahrenheit that converts Celsius to
Fahrenheit and prints the result. (Formula: (Celsius * 9/5) + 32 = Fahrenheit).
"""

celsius: float = float(input("Enter temperature in Celsius: "))


def celsius_to_fahrenheit(celsius):
    Fahrenheit = (celsius * 9 / 5) + 32
    print(f"Conversion of celsius to fahrenheit is {Fahrenheit} value.")


celsius_to_fahrenheit(celsius)
