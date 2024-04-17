class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """    
        for part in range(len(haystack)):
            if haystack[part:part+len(needle)] == needle:
                return part
            
        return -1