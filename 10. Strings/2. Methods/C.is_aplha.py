a = "harshal a py fullstack dev"
v = a.isalpha()
print(v)
# False q ki bich mai space hai usko special treatment mt do
# if i remove space
y = "harshalapyfullstackdev"
o = y.isalpha()
print(o)  # True


m = y.isalnum()  # kya y var mai yaa to alphabet ya num ya dono ka mixture hai ?
print(m)  # True

l = y.isdigit()  # kya sab k sab digits hai y var mai
print(l)  # false
