class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        
        happy_deltakere = 0
        j = 0

        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1
                
            if j < len(s):
                happy_deltakere += 1
                j += 1
                        
        return happy_deltakere