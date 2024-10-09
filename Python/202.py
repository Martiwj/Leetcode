class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            digits = map(lambda x: int(x), str(n))            
            n = sum(map(lambda x: x ** 2, digits))
        
        return n == 1