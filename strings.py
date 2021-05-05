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

# def are_you_playing_banjo(name):
#     if name[0].lower() == "r":
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# areYouPlayingBanjo = lambda n: n+[" does not play banjo"," plays banjo"][n[0].lower()=='r']

# >>>>>>>>>>>>>>

# FIX-ERROR

# def get_status(is_busy):
#     status = "busy" if is_busy else "available"
#     return status

# Function should return a dictionary/Object/Hash with "status" as a key, 
# whose value can : "busy" or "available" depending on the truth value of the argument is_busy.

# def get_status(is_busy):
#     status = "busy" if is_busy else "available"
#     return {"status" : status}

# >>>>>>>>>>>>>>

# The company you work for has just been awarded a contract to build a payment gateway. 
# In order to help move things along, you have volunteered to create a function that will take a 
# float and return the amount formatting in dollars and cents.

# 39.99 becomes $39.99

# The rest of your team will make sure that the argument is sanitized before being passed to
#  your function although you will need to account for adding trailing zeros if they are missing 
#  (though you won't have to worry about a dangling period).

# def format_money(amount):
#     num = str(amount)
#     rvrs = num[::-1]
#     dot = rvrs.find(".")
#     if dot == 1:
#         rvrs = "0" + rvrs
#         return "$" + rvrs[::-1]
#     elif dot == 2:
#         return "$" + rvrs[::-1]
#     else:
#         rvrs = "00." + rvrs
#         return "$" + rvrs[::-1]
# print(format_money(98))

# or
# def format_money(amount):
#     return '${:.2f}'.format(amount)
# print(format_money(98))

# >>>>>>>>>>>>>>

# fix
# def build_string(*args):
#     return "I like {}!".format(",".join(args))


# def build_string(*args):
#     return "I like {}!".format(", ".join(args))

# or

# def build_string(*args):
#     return f"I like {', '.join(args)}!"