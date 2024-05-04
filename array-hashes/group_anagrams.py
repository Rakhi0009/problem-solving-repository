# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

import sys
from valid_anagram import valid_anagram

strs = sys.argv[1]

def group_anagram(strs):
    map_dict ={}
    result_list = []

    for i in range(len(strs)):
        temp_list =[]
        if strs[i] not in map_dict.keys():
            temp_list.append(strs[i])
            map_dict[strs[i]] = 0
        else:
            continue

        j = i+1
        while j < len(strs):
            is_anagram = valid_anagram(strs[i], str[j])
            if is_anagram:
                temp_list.append(strs[j])
                map_dict[strs[j]] = 0
            j+=1
        if temp_list != []:
            result_list.append(temp_list)
    return result_list




