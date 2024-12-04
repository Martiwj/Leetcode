class Solution:
    def maximumGap(self, nums: List[int]) -> int:
    
        if len(nums) == 1:
            return 0
        
        nums.sort()
        max_dist = 0
        for i in range(1,len(nums)):
            if (diff := nums[i] - nums[i-1]) > max_dist:
                max_dist = diff 

        return max_dist


