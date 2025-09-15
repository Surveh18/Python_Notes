# lambda - Anonymous
def add_numbers(n1, n2, n3):
    # No logic is written here
    return n1 + n2 + n3


# upr k function mai hum 3 parameters le rhe hai
# or unka sum return kr rhe hai lekin humne andr koi logic nhi likha func mai
# to jha 2 line use hui hum ek line mai kr skte hai.

lambda n1, n2, n3: n1 + n2 + n3
# isme bhi same chizz ho rhi hai
# 3 parameters liye or output diya
# isme return likhne ki zaroorat nhi hai
# bydefault return hi hota hai

# ab yaha is function ka koi naam nhi hai to use krne k liyee
# isko ek variable mai store karenge.

add_number = lambda n1, n2, n3: n1 + n2 + n3
print(f"By using lambda function = {(add_number(10,20,30))}")
