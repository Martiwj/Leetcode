from collections import defaultdict

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        
        for i, j in zip(s, t):    
            freq1[i]+=1
            freq2[j]+=1
        

        return freq1 == freq2