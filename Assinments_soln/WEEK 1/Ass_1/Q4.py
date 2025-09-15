"""
Ask value in rupee and convert into paise.
"""

Rupee: int = int(input("Enter value in rupees: "))
Paise: int = Rupee * 100
print(f"{Rupee} Rupees is equal to {Paise} Paise")
