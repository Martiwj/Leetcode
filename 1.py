class Solution(object):
    def twoSum(self, nums, target):
        maps = {}
        for i, num in enumerate(nums):
            if (target-num) in maps:
                return [maps[target-num], i]

            maps[num] = i

        return []
    
    