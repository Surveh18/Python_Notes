"""
Q4. Ask x and n from user and then calculate the following answer.
# Example 1
pattern (x=6, n=4)

# Output
6^1 - 6^3 + 6^5 - 6^7
-272370 (OUTPUT)


# Example 1
pattern (x=9, n=11)

# Output
9^1 - 9^3 + 9^5 - 9^7 + 9^9 .... upto n times
108084611215274403609(OUTPUT)

"""


def xn_2(x, n):
    flag = True
    total = 0
    exp = 1
    for i in range(1, n + 1):
        if flag == True:
            total = total + (x**exp)
            exp = exp + 2
            flag = False
        else:
            total = total - (x**exp)
            exp = exp + 2
            flag = True
    return total


print(xn_2(6, 4))
print(xn_2(9, 11))
