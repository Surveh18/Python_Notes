# ek str mai agr kuch bhi diya ho capital,upper case mai to usko lower case mai kese kare
a = "HELLO BETAA KESE HO ?"
b = a.lower()
# Return a copy of the string converted to lowercase.
# list immutable hai a mai koi changes nhi honge isliye b mai store kr rhe hai uski copy
print(b)
# hello betaa kese ho ?
# means here hum a mai koi chnage nhi kr rhe hai
# same for upper
# c = a.upper()


# title
s = "haRSHAL iS a coDER"
t = s.title()
print(t)  # Harshal Is A Coder
# title matlab har word ka pehla letter capital

# swapcase - Convert uppercase characters to lowercase and lowercase characters to uppercase.
n = s.swapcase()
print(n)  # HArshal Is A COder
