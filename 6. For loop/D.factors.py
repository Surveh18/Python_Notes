# n: int = 10
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")
"""
Logic to find factors:-
suppose we have to print factors of 10 which are (1,2,5,10).

so lets find out 
- 10 is divisible by 1 - Yes
- 10 is divisible by 2 - Yes
- 10 is divisible by 3 - No
- 10 is divisible by 4 - No
- 10 is divisible by 5 - Yes
- 10 is divisible by 6 - No
- 10 is divisible by 7 - No
- 10 is divisible by 8 - No
- 10 is divisible by 9 - No
- 10 is divisible by 10 - Yes
"""
i = 1
m = 10
while i <= m:
    if m % i == 0:
        print(i, end=" ")
    i += 1
