"""
Que - Ask a file name, Keep asking the sentence until user quiets
"""

file_name = input("Enter file name (without extension): ")
file_name = file_name + ".txt"

with open(file_name, "w") as f:
    while True:
        sentence = input("Enter sentance: ")
        if sentence == "q" or sentence == "Q":
            break
        f.write(sentence + "\n")
