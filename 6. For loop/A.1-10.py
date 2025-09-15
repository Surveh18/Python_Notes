"""
for loop syntax:
for i in range(start,stop-1,step)
    print(i,end=" ")
    statements....

i - variable_name
in - membership_operator
range - function(to start the loop)
start(inclusive) - by default it starts from 0.
stop(exclusive) -  it does'nt counts the last digit.
suppose start - 0 stop - 5 
output will be 0 1 2 3 4 
steps - how many numbers we want to skip.
"""

start_up = int(input("Enter start: "))
end_up = int(input("Enter end: "))

for i in range(start_up, end_up + 1):  # by default for loop starts from 0.
    print(i, end=" ")

"""
when to use for loop:- when we know the ending part.

when to use while loop:- when we have to iterate through condition bases.

in - membership operator

while loop execution is much faster than for loop.

"""
