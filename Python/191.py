class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = str(bin(n)[2:])
        return sum(1 for b in bits if b == "1")