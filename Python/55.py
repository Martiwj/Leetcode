class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        goal = n-1

        for i in range(n-1,-1,-1):
            jump = nums[i]

            if i + jump >= goal:
                goal = i

        return True if goal == 0 else False