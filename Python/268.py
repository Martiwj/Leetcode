class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0

        for i, n in enumerate(nums):
            count -= n 
            count += i+1
        return count 
        
