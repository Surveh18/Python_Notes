def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()

"""
Steps:-
filhal upr ka likha bhul jao n line 10 se shuru krte hai
normally func define hai ordinary naam se uske andr print statement hai
fir call kiya kaayde se I am ordinary print hona chaiye

pr uske upr @make pretty hai matlab ek decorator yaani ki uska code pehle run hoga
baad mai apna ordinary function run hoga 

ab @make preety mai kya hai ek func hai uska param mai ek or func hai jiske andr apna 
ordinary function jaayega fir inner run hoga uska print statement chalega
fir wapis ek func hai jo ki hmara ordinary function hai fir return karega
"""
