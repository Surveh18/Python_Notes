"""
Q18. Create a function that finds how many prime numbers there are, up to
the given integer.

• prime_numbers(10) -> 4
  ° # 2, 3, 5 and 7

• prime_numbers(20) -> 8
  ° # 2, 3, 5, 7, 11, 13, 17 and 19

• prime_numbers(30) -> 10
  ° # 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29
"""


def prime_num(n):
    cnt = 0
    for i in range(2, n + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            cnt += 1
    return cnt


print(prime_num(10))
print(prime_num(20))
print(prime_num(30))
