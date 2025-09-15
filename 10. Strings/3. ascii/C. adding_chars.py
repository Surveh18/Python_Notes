# ans = ""
ans = str()  # the good way to declare an empty str
while True:
    char = input("Enter chars: ")
    # if char == "q" or char == 'Q': the ideal way is this acc to time complexity.
    if char in ["q", "Q"]:
        break
    else:
        ans += char
print(ans)
print(type(ans))
"""
every time we are assigning a char in ans variable its reassigning into a new variable
str are immutable but concatination is possible.
"""

a = "Harshal"
print(id(a))  # 1711038900592

a += "Surve"
print(id(a))  # 1711039116208

a += "Xyz"
print(id(a))  # 1711039116144
print(a)  # HarshalSurveXyz
