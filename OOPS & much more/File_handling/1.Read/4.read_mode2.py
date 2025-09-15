with open("Hello.txt", "r") as f:
    # print(f.read())

    # We can also iterate through if
    # we are saving as f so lets iterate f
    # for ch in f:
    #     print(ch)
    # Iterating only single character
    x = f.read()
    for i in x:
        print(i)

"""
# OUTPUT :-
print By-default leaves one line thats why we have spaces between them.
=== Motivational Quotes ===

1. "The only way to do great work is to love what you do." â€” Steve Jobs

2. "It always seems impossible until itâ€™s done." â€” Nelson Mandela

3. "Do one thing every day that scares you." â€” Eleanor Roosevelt
"""
