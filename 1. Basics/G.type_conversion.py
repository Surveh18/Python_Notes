"""
Type_Conversion / Type_Casting

int -> str
str -> int
float -> str
float -> int
str -> list
list -> str
int -> dict
"""

#1
# a = "python"
# b = "Language"
# print(a + b)

# output - pythonlanguage

#2
# a = "python"
# b = "11"
# print(a + b)

# output- python11

#3
# a = "python"
# b = str(11)
# print(a + b)
# output - python11


#4
# a = "100"
# b = "300"
# print(a + b)

# output - 100300

#5
# a = int("00100")
# b = int("300")
# print(a + b)

# output - 400 (it will eliminate starting 00 from a variable)

#6
a = int("100abc") #here variable nameing conventions are not fullfilled.
b = int("300")
print(a + b)

# output - ValueError

#7
# a = int("100.55")
# b = int("300")
# print(a + b)

# output - ValueError

#8
# a = float("100.55")
# b = int("300")
# print(a + b)

# output - 400.55

#9
# a = float(10)
# print(a)

# output - 10.0

#10
# a = int(10.9)
# print(a)

#output - 10

#11
# a = int(-10.9)
# print(a)
#output - (-10 int converts to the nearest zero).

#12
# a = int(-56.9999)
# print(a)
#output - (-56)





