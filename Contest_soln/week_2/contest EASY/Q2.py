# Q2. Print all the prime numbers between 1 to 100.
for number in range(2, 101):  # 2 se 10 tak numbers
    is_prime = True  # Maan ke chalte hain number prime hai

    for divisor in range(2, number):  # 2 se lekar number-1 tak
        if number % divisor == 0:  # Agar number divisible hai, toh break
            is_prime = False
            break  # Number ko prime nahi maanenge, loop se nikal jao

    if is_prime:  # Agar number prime hai, toh print karo
        print(number, end=" ")
