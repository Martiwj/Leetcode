class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        ans = []
        sub_arr = [nums[0]]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:  
                ans.append(sub_arr)
                sub_arr = []
            sub_arr.append(nums[i])
        
        if sub_arr:
            ans.append(sub_arr)
        
        ans = [f"{min(a)}->{max(a)}" if len(a) > 1 else f"{min(a)}" for a in ans]
        
        return ans