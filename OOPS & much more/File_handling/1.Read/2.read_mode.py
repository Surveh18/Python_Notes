"""
# Read means jo bhi file hai uska content read krna
Before doing read ek txt file create kr k uske andr ka content read krneka try krte hai

so read mode krne k liye variable bnate hai f naam ka uske jagah hum koi bhi naam ka variable le skte hai
"""

# f = open("C:\\Users\\surve\\OneDrive\\Documents\\AI-ML\\Python\\File_handling\\3.txt")
# double \\ q ki agr single karenge to escape seq mai count hoga vo but hum ek folder k andr sab kr rhe hai isliye

# hover on open iska bydefault readmode rehta hai n uskp close bhi krna hota hai
# Open n close k biche mai aap kuch bhi perform kr skte ho
f = open("Hello.txt", "r")
# x = f.read()
# print(x)
print(f.readline())  # this will give a single line.
print(f.readlines())  # this will give lines in list format.

"""
read() - Full content display hoga file ka 
read(5) - Only 5 letters

-Now python uses an imaginary cursor so
if i do read(5) - 1st 5 letters print karega 
then if i do again read(5) - another 5 letters nxt
"""

f.close()
