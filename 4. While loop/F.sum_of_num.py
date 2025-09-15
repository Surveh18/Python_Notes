# 1 to 10,by adding (print Total)
# 1+2+3+4+5+6+7+8+9+10 = 55
def totalSum():
    i = 1
    total = 0
    while i <= 10:
        total = total + i
        i += 1
    return total


x = totalSum()
print(f"Your total is {x}")
