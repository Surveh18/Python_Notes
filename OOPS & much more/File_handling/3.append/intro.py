# Append is used to add new line while maintaing the existing content.
# It also create a new file if file doesn't exist.
with open("Hello.txt", "a") as f:
    f.write("\nA new line")
