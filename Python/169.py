from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenght = len(nums) // 2
        freqs = defaultdict(int)
        
        for num in nums:
            if freqs[num] >= lenght:
                return num
            freqs[num] += 1
            
    
    
