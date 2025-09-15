# QI. 2 22 222 2222 22222 ... upto n. (Ask n from user)
def var2(n: int):
    i: int = 1
    x: int = 2
    while i <= n:
        print(x, end=" ")
        x = x * 10 + 2
        i += 1


n = int(input("Enter number: "))
var2(n)
