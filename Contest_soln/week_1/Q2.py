"""
Q2. Given three angles of a triangle, determine whether it is an acute,
obtuse, or right-angled triangle.
"""

# here we will be considering 3 angles of Triangle.(a,b,c)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Squared sides of traingle.
a_squared = a**2
b_squared = b**2
c_squared = c**2


def traingle_angle(a, b, c):
    if a_squared + b_squared == c_squared:
        print("It is Right_angled triangle.")
    elif a_squared + b_squared > c_squared:
        print("It is Acute angle.")
    elif a_squared + b_squared < c_squared:
        print("It is Obtuse angle.")


traingle_angle(a, b, c)
