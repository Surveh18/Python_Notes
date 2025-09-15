# convert to lower case. we will use result variable beacuse str is immutable
a = "HARshAL$#^!   *@@#000ADwerHHDFOA  ___++"
result = str()
# - 65-90           | A to Z     | Uppercase letters
# - 97-122          | a to z     | Lowercase letters
# upper case k chr mai 32 add karo to lower case bn jaata hai 65 + 32 = 97
print(chr(97))  # a
print(ord(chr(97)))  # 97
for ch in a:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <= 90:
        ascii_code += 32
        new_char = chr(ascii_code)
        result += new_char
    else:
        result += ch
print(result)
# harshal$#^!   *@@#000adwerhhdfoa  ___++
