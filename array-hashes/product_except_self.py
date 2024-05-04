#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#You must write an algorithm that runs in O(n) time and without using the division operation.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,4]
#Output: [24,12,8,6]
#Example 2:
#
#Input: nums = [-1,1,0,-3,3]
#Output: [0,0,9,0,0]
# 
#
#Constraints:
#
#2 <= nums.length <= 105
#-30 <= nums[i] <= 30
#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

import sys
import math
nums = sys.argv[1]

def productExceptSelf_v1(nums):
    first_index = 0
    last_index = len(nums)
    result_list = []
    for i in range(last_index):
        first_half = math.prod(nums[first_index:i])
        second_half = math.prod(nums[i+1:last_index])
        product = first_half * second_half
        result_list.append(product)
    return result_list

def productExceptSelf_v2(nums):
    temp_nums = nums.copy()
    result_list =[]
    for i in range(len(nums)):
        temp_nums[i] = 1
        product = math.prod(temp_nums)
        result_list.append(product)
    return result_list

def productExceptSelf_v3(nums):
    prefix_list , postfix_list = [] , []
    prefix = postfix = 1
    for i in range(len(nums)):
        prefix_list.append(prefix)
        prefix *=nums[i]
    for j in range(len(nums)-1,-1,-1):
        postfix_list.append(postfix)
        postfix *= nums[j]
    high = len(nums)-1
    for k in range(len(nums)):
        prefix_list[k] = prefix_list[k]*postfix_list[high]
        high -= 1
    return prefix_list
