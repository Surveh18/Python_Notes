"""
Truthy Falsy

int -> 0 (Falsy), 1,2,3,-1,-2 (Truthy)
float -> 0.0 (Falsy), 1.2, 2.8, 3.1, -1.111, -2.22, 0.003 (Truthy)
str -> "" (Falsy), "Surve", " ", "!", "dwuu233" (Truthy)

"""
# if knows boolean  
num = " "
if num:
    print("yes")
else:
    print("No")
