# Whitespaces -> \n, \t, Space

my_string = "Python is a good language"
# case 1
ans = my_string.split()
# by default split ko koi value naa mile to whitespaces se split kr deta hai

# case 2
ans1 = my_string.split("a")
print(ans)
# ['Python', 'is', 'a', 'good', 'language']

print(ans1)
# ['Python is ', ' good l', 'ngu', 'ge']
