try:
    lst3 = [22, 45, 32, 78, 90, 0]
    print(lst3[0])
    # print(lst3[22])  # 22 index-out-of-range so error
    # print(lst3[0] / lst3[-1])  # 22 cannot be divide by 0
except IndexError:
    print("Invalid Index")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Some error occour")
else:
    print("Everything worked fine")

"""
This else part is optional not compulsory
this else block will execute only if upr k try block mai koi error naa aaye
"""

"""
Output:-
22
Everything worked fine
"""
