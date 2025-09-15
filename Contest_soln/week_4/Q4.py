"""
Q4. Ask a sentence from user. Then ask a integer k from user.
Print all the words which are greater or equal to k
"""


def sentence1(n: str, k: int):
    words = n.split()
    result = []
    for w in words:
        if len(w) >= k:
            result.append(w)
    print(f"Result = {" ".join(result)}")


sentence = input("Enter the sentence: ")
k = int(input("Enter the digit: "))
sentence1(sentence, k)
