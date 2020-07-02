###########description#########
#1. Two Sum

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

##########testcase###########
#nums = [7, 11, 15, 2]
#target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            c = 0
            if target - nums[c] == nums[i]:
                return([c, i])
            c+=1                 

#output:[0,1]            
            