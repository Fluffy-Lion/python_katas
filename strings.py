# starting locations of anagrams
# from collections import Counter

# def is_anagram(s1 , s2):
#     return Counter(s1) == Counter(s2)

# def anagram_indices(word, s):
#     result = []
#     for i in range(len(s) - len(word) + 1):
#         window = s[i:i + len(word)]
#         if is_anagram(window, word):
#             result.append(i)
#     return result

# print(anagram_indices("ab", "abwvaba"))

# >>>>>>>>>>>>>>

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# areYouPlayingBanjo = lambda n: n+[" does not play banjo"," plays banjo"][n[0].lower()=='r']