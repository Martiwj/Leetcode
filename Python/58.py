class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        last_word_length = len(s[len(s)-1])
        return last_word_length
    
    