"""
Q7. Create a function named as printPrimeFactors that takes an integer n
as a argument and print all the prime factors of that number.

Example if number = 20

Then the factors of 20 are 1,2,5,10,20.

So prime factors are 2,5 (this is the output)

printPrimeFactors(20)
printPrimeFactors(7)
printPrimeFactors(72)

# Output
2 5
7 
2 3

workflow:
1.printPrimefactorS(num):
-> Find all the factors of the given num (factors are numbers that divide it 
without a remainder which is zero.)

->For each factor, check if it is prime using the checkPrime function.

-> If the factor is prime, print it.

"""


def factors(num):
    fact = 0
    i = 1
    while i <= num:
        if num % i == 0:
            fact += 1
        i += 1
    if fact == 2:
        return True
    else:
        return False


def printPrimeFactors(num):
    i = 1
    while i <= num:
        if num % i == 0:
            if factors(i):
                print(i, end=" ")
        i += 1


printPrimeFactors(20)
"""
Step-by-Step Execution for printPrimeFactors(20):
1.Start with num = 20.
2.Call printPrimeFactors(20):
-> Initialize i = 1.
-> Use a while loop to check all numbers from 1 to 20.

Iteration 1:
-> i = 1.
-> 20 % 1 == 0 (1 is a factor of 20).
-> Call factors(1):
  -Count factors of 1:
    -1 % 1 == 0 → fact = 1.
    -fact != 2 → 1 is not prime → return False.
-> Skip printing 1.

Iteration 2:
->i = 2.
->20 % 2 == 0 (2 is a factor of 20).
->Call factors(2):
  -Count factors of 2:
    2 % 1 == 0 → fact = 1.
    2 % 2 == 0 → fact = 2.
    fact == 2 → 2 is prime → return True.
->Print 2.

Iteration 3:
i = 3.
20 % 3 != 0 (3 is not a factor of 20).
Skip 3.

Iteration 4:
->i = 4.
->20 % 4 == 0 (4 is a factor of 20).
->Call factors(4):
  -Count factors of 4:
    -4 % 1 == 0 → fact = 1.
    -4 % 2 == 0 → fact = 2.
    -4 % 4 == 0 → fact = 3.
    -fact != 2 → 4 is not prime → return False.
->Skip printing 4.

Iteration 5:
->i = 5.
->20 % 5 == 0 (5 is a factor of 20).
->Call factors(5):
  -Count factors of 5:
    -5 % 1 == 0 → fact = 1.
    -5 % 5 == 0 → fact = 2.
    -fact == 2 → 5 is prime → return True.
->Print 5.

Continue for i = 6 to i = 19:
->Factors: Only 10 divides 20, but it is not prime.

Iteration 20:
->i = 20.
->20 % 20 == 0 (20 is a factor of 20).
->Call factors(20):
  -Count factors of 20:
    -20 has more than 2 factors → not prime → return False.
->Skip 20.

Output:
The prime factors of 20 are:
2 5
"""
