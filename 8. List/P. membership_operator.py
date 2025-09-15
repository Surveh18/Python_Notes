# IN, NOT IN
my_list = [45, 65, 43, "Harshal", "python is gud language", 11]
# Suppose i want to know if 45 exist is my list ??
# Method 1:
x = 45
if my_list.count(x) >= 1:
    print("Yes")
else:
    print("No")

# Method 2:
if x in my_list:
    print("Yes")
else:
    print("No")

# Method 3:
print(x in my_list) #True - means exists.
