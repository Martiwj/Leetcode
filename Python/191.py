class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = str(bin(n)[2:])
        return sum(1 for b in ans if b == "1")