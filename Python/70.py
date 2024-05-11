class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        steps = [1,2]
        
        if n <=2:
            return steps[n]

        for i in range(2, n+1):
            steps.append(steps[i-1]+steps[i-2])

        return steps[n-1]