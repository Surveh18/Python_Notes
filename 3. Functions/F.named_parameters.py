# Function Decalaration / Creation
def marks(phy: float, chem: float, maths: float, eng: float):
    total = phy + chem + maths + eng
    print(f"Total marks scored is {total}")


# Function calling & passing argumnets.
marks(eng=33, phy=41, maths=77, chem=38)
# Suppose i want to pass marks in illogical order it can written as.

marks(22, 76, eng=79, maths=56)
# in above if i want to pass phy n chem marks regularlly.
# then eng n maths according to me it can be pass in this way.
# but we cannot do it like this marks(maths=56,eng=79,22,76) it is incoorect way.
