#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
#You must write an algorithm that runs in O(n) time.
#
#
#
#Example 1:
#
#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#Example 2:
#
#Input: nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9
#
#
#Constraints:
#
#0 <= nums.length <= 105
##-109 <= nums[i] <= 109

import sys
nums = sys.argv[1]

def longest_consective_sequence(nums):
    if len(nums) == 0:
        return 0
    max_len = 1
    count = 1
    for i in range(len(nums)-1):
        j = i+1
        if nums[i] == nums[j]:
            continue
        if abs(nums[j]-nums[i]) == 1:
            count +=1
        else:
            count = 1
        max_len = max(max_len,count)
    return max_len

print(longest_consective_sequence(nums))
    
    
