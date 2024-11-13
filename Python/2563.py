class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        
        for i in range(n - 1):
            low = lower - nums[i]
            high = upper - nums[i]
            
            left = bisect_left(nums, low, i + 1, n)
            right = bisect_right(nums, high, i + 1, n) - 1
            
            if left <= right:
                count += (right - left + 1)
        
        return count