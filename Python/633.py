import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0: return False
        
        for a in range(int(math.sqrt(c)+1)):
            b_sqaure = c - a**2
            b = int(math.sqrt(b_sqaure))
            
            if b**2 == b_sqaure: return True
            
        return False