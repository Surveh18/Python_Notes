# What is exception handling ?

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst1[1])  # 2
# print(lst1[65])  # out-of-range so error
# Ab 65 out of range hai lekin baaki niche k elements to exist krte hai to unka output to we should get
# But program hmara error through kr k ruk jaayega aage nhi badhega isliye we use exception handling.
print(lst1[3])  # 4
print(lst1[4])  # 5
print(lst1[5])  # 6


try:
    lst2 = [13, 22, 34, 64, 15, 66]
    print("----Try block----")
    print(lst2[1])  # 22
    print(lst2[33])  # Out-of-range so error
    print(lst2[3])  # 64
    print(lst2[4])  # 15
except:
    print("Some error Occured")

print("Done")
print("OKk")

"""
Output : -
----Try block----
22
Some error Occured
Done
OKk

# So print(lst2[33])  # Out-of-range so error lekin hmara program nhi rukega 
# aage k 2 print statement bhi execute krega
So same chiz hum production level pr bhi assume kr skte hai ki kuch ho to hmara program nhi rukna chaiye
"""
