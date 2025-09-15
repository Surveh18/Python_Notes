# Q9. Ask a number from user Print if that number is prime or not, use Functions.
def fact(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not prime")


fact(2)
fact(4)
"""
# using while loop
def fact(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    if count == 2:
        print("Prime")
    else:
        print("Not prime")

"""
