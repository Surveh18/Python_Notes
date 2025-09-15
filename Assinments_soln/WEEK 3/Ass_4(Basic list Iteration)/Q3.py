# Q3. Make a list of your own. Count how many numbers are divisible by 5.
my_list = [54, 67, 1, 43, 67, 100, 45, 32, 74, 51, 40]
count = 0
n = len(my_list)
for i in range(0, n):
    if my_list[i] % 5 == 0:
        count += 1
print(count)

cnt = 0
for num in my_list:
    if num % 5 == 0:
        cnt += 1
print(cnt)
