"""
Que - Take num from user and check whether its
zero, positive, or negative.

"""

num = -1
if num >= 0:
    # if num >=0 then num must be zero or positive else num will be -ve.
    if num == 0:
        print("zero")
    else:
        print("positive")
else:
    print("negative")
