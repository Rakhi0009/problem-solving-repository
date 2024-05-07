# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

import sys

s , t = sys.argv[1] , sys.argv[2]

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    for char in s:
        if char not in t:
            return False
        t = t.replace(char,'',1)

    return True