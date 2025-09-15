# Q1. Use a while loop to calculate the sum of the first 10 natural numbers.
# 1+2+3+4+5+6+7+8+9+10 = 55

i = 1
total = 0
while i <= 10:
    total = total + i
    i += 1
print(f"The sum of first 10 natural numbers is {total}.")
