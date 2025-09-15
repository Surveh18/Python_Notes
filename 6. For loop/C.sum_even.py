def sum_even(start_up: int, end_up: int) -> int:
    total: int = 0
    for i in range(start_up, end_up + 1):
        if i % 2 == 0:
            total = total + i
    return total


start_up: int = int(input("Enter start num: "))
end_up: int = int(input("Enter end num: "))
print(f"The sum of even numbers is {sum_even(start_up,end_up)}.")
