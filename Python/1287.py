from collections import defaultdict

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = defaultdict(int)
        for i in arr:
            freq[i] +=1 
            if freq[i] > 0.25 * len(arr):
                return i
        return