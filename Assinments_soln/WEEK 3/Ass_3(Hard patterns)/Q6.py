n = 9
for i in range(n // 2 + 1, 0, -1):
    for j in range(i, n // 2 + 2):
        print(j, end=" ")
    print()
for k in range(1, n // 2 + 1):
    for p in range(k + 1, n // 2 + 2):
        print(p, end=" ")
    print()
"""
2 3 4 5
3 4 5 
4 5 
5  
"""

"""
5
3 4 5
2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5 
5
"""
