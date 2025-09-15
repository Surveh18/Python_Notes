# Q1. There are two variables
a = 5
b = 10
"""
 What will be the output of following:
A. a>5 and b>=10
B. a>=5 or not b>10
C. not(a>5 and b>5)
D. not(a<10 or not b<10)
E. not(not a<=5 or not b>=10)
"""
print(a > 5 and b >= 10)
# FALSE

print(a >= 5 or not b > 10)
# TRUE

print(not (a > 5 and b > 5))
# TRUE

print(not (a < 10 or not b < 10))
# FALSE

print(not (not a <= 5 or not b >= 10))
# TRUE
