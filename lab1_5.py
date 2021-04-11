
#problem5 remove_vowels

import re

def remove_vowels(string):
    return (re.sub("[aeiouAEIOU]", "", string))

# second solution

# def remove_vowels(s):
#     vowels = ('a', 'e', 'i', 'o', 'u') 
#     for c in s.lower():
#         if c in vowels:
#             s = s.replace(c, "")
#     return s

print(remove_vowels("Mobile"))