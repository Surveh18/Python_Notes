for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")

    for k in range(5, 5 - i, -1):
        print(k, end=" ")
    print()


"""
        5 
      5 4
    5 2 3
  5 4 3 2
5 4 3 2 1
"""
