from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_set = set(jewels)

        return sum(stone in jewel_set for stone in stones)