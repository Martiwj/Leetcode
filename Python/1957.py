class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) <3:
            return s
        
        new_s = [s[0]]
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                new_s.append(s[i])
        
        return "".join(new_s)