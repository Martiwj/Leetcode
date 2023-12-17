class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = list(s)

        for i in range(0, len(s_list), 2*k):
            s_list[i:i+k] = reversed(s_list[i:i+k])
        
        result = ''.join(s_list)

        return result
    