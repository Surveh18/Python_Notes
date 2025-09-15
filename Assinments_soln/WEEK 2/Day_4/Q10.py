"""
Q10.ask a number from user n1.
From 1 to n1, print how many prime numbers are there.
"""


def primeCount(n1):
    count = 0
    for number in range(2, n1 + 1):  # 2 se 10 tak numbers
        is_prime = True  # Maan ke chalte hain number prime hai

        for divisor in range(2, number):  # 2 se lekar number-1 tak
            if number % divisor == 0:  # Agar number divisible hai, toh break
                count += 1
                is_prime = False
                break  # Number ko prime nahi maanenge, loop se nikal jao
    print(count)


primeCount(100)
