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
finally:
    print("This is finally clause part")
"""
It is not compulsory k else part likha to finallly bhi likhna zaruri hai
There might bhi possible ki aap sirf finally likho n else part nhi ya dono bhi likh skte hai
But main part bhi finally clause hmesha run hoga no matter try part mai error hai ya nhi  


# Output - With error
Invalid Index
This is finally clause part

# Output - Without error
22
Everything worked fine
This is finally clause part
"""
