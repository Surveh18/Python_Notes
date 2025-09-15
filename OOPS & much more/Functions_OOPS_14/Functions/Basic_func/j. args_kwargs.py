# Prerequest mai tuple seekhna pdega
def add(*args):
    print(args)


# ye hum tab use krte hai jab hme nhi pta ki hm kitne arguments pass krne vaale hai.
# args mai pass kiye arguments tuple mai convert ho jaate hai
# *args - arguments (ye tuple hota hai)
# **kwargs - keyword arguments (ye dictionary hoti hai)


def sub(*num):
    print(num)


# *args ye koi keyword nhi hai pr normally hrr jagah yhi use krte hai
#  star(*) kr k koi bhi naam likh skte hai.


def info(*args, **kwargs):
    print(kwargs)
    print(args)


info(name="surve", age=24, gen="Male")
# agr hum named parameters use karenge to vo kwargs mai jaayega
# which will convert in dictionary or agr normally arguments pass karenge to args mai jaayega
info("Harshal", 24, "Male")
