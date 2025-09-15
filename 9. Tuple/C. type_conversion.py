a = (54, 43, 11, 91, 92)
print(f" Id of 1st a = {id(a)}")
# suppose i want to add 100 value in a tuple eese to add kr nhi skte
# so list mai convert karenge a ko
b = list(a)
print(b)
# [54, 43, 11, 91, 92] - as we can see list mai convert ho gyi hai
b.append(100)
print(b)  # [54, 43, 11, 91, 92, 100]

a = tuple(b)
print(f" Id of 2nd a = {id(a)}")
print(a)  # (54, 43, 11, 91, 92, 100)
