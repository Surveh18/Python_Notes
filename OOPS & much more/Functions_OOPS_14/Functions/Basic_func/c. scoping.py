def add():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    print(f"Ans = {num1+num2}")
    # num1 and num2 variable are only valide inside add() function - LOCAL SCOPE


def sub():
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    print(f"Ans = {num1-num2}")
    # here num1 and num2 variable are also having local scope inside function.


add()
sub()


# both num1 & num2 variable in both function aree different.
