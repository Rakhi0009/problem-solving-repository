# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

import sys

nums , k = sys.argv[1] , sys.argv[2]

def top_k_frequent_ele_v1(nums,k):
    num_set = set(nums)
    map_dict = {}
    result_list = []

    for ele in num_set:
        map_dict[ele] = nums.count()
    
    map_dict = sorted(map_dict.items(),key= lambda x : x[1] , reverse=True)

    for i in map_dict:
        if k == 0:
            break
        result_list.append(map_dict[i])
        k -= 1
    return result_list

def top_k_frequent_ele_v2(nums,k):
    num_set = set(nums)
    map_dict = {}
    result_list = []

    for ele in num_set:
        map_dict[ele] = nums.count()
    
    for i in range(k):
        key = max(zip(map_dict.values,map_dict.keys))[1]
        result_list.append[key]
        del map_dict[key]
    return result_list

