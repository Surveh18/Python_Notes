"""
Q4. Create a dictionary that counts the frequency of words in a given string.
Ask string from user.
Example 1
Input String: "The sun is shining and the weather is nice"
Output:{
         'The': 1,
         'sun': 1,
         'is': 2,
         'shining': 1,
         'and': 1,
         'the': 1,
         'weather': 1,
         'nice': 1
        }

Example 2
Input String: “The cat and the dog played in the park The cat chased the dog”
Output:{
         'The': 2,
         'cat': 2,
         'and': 1,
         'dog': 2,
         'played': 1,
         'in': 1,
         'the': 3,
         'park': 1,
         'chased': 1
        }
"""

String = "The sun is shining and the weather is nice"
freq_map = dict()
words = String.split()
for ch in range(0, len(words)):
    if words[ch] in freq_map:
        freq_map[words[ch]] += 1
    else:
        freq_map[words[ch]] = 1
print(dict(freq_map))


def wordCount(s: str):
    freq_map = {}
    for word in s.split():
        freq_map[word] = freq_map.get(word, 0) + 1
    return freq_map


s = "The sun is shining and the weather is nice"
String = "The cat and the dog played in the park The cat chased the dog"
print(wordCount(s))
print(wordCount(String))
