"""
Q2. Create a function named arrangeChars which takes a string as a parameter.
Now return a string with max frequency chars at start.
print (arrangeChars ( "aaeroplane" ) )
# Output
aaaeeropln
print ( arrangeChars ( "heelllllooo' ) )
# Output
llllloooeeh
"""

n = "aaeroplane"
result = ""
for ch in n:
    if ch not in result:  # agar pehle add nahi hua
        count = n.count(ch)  # string me frequency count karo
        result += ch * count  # repeat character count times

print(result)
