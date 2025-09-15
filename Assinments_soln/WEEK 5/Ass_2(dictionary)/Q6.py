"""
Q6. Ask a string from user. Store the frequency of each character in the dictionary. Then print the character with the maximum frequency.
Input:
Please enter a string: hello world
Output:
The character with the maximum frequency is 'l'
"""

n = "Hello world"
freq = {}
for i in range(0, len(n)):
    if n[i] in freq:
        freq[n[i]] += 1
    else:
        freq[n[i]] = 1
max_char = max(freq, key=freq.get)
print(f"The character with the maximum frequency is '{max_char}'")
