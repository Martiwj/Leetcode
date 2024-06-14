class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        moves = 0
        
        n = len(nums)
        
        prev = nums[0]
    
        for i in range(1, n):
            
            if nums[i] <= prev:
                moves += (prev + 1 - nums[i])
                nums[i] = prev + 1
                
            prev = nums[i]
        
        return moves
