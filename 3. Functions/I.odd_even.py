"""
Function which takes one integer arguments
return a string, ODD, EVEN.
"""

num = int(input("Enter the num: "))


def even_odd_check(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


ans = even_odd_check(num)
print(ans)


# Alternative
# def adder(num: int) -> str:
#     if num % 3 == 0:
#         return "Odd"
#     return "Even"


# Above is just for understanding that we can write without using else also.
# Its also known as clean coding.
# adder_ans = adder(54)
# print(adder_ans)
