"""
1. we know index error in list elements if list is out-of-range
So IndexError ye ek Exception ka naam hai

2.print(10/0) - in maths we know ans is infinity but in python
ZeroDivisionError: division by zero
"""

# So we can have multiple exception.

try:
    lst3 = [22, 45, 32, 78, 90, 0]
    print(lst3[22])  # 22 index-out-of-range so error
    print(lst3[0] / lst3[-1])  # 22 cannot be divide by 0
except IndexError:
    print("Invalid Index")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Some error occour")
"""
We can see line by line execute hoga print(lst3[22]) index error k block mai jaayega
if print(lst3[22]) ko comment kare to next line execute hogi n ZeroDivisionError vala except execute hoga
"""
