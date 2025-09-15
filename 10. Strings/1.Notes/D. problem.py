a = "Hello WOOrLLDd"
# count kitne o hai a mai

# Via value
count = 0
for i in a:
    if i == "o" or i == "O":
        count += 1
print(count)  # 3

# Via index
count1 = 0
for ch in range(0, len(a)):
    if a[ch] == "o" or a[ch] == "O":
        count1 += 1
print(count1)  # 3
