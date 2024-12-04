class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        c = 0
        j = 0
        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                c += 1
                j += 1 
                
        return len(s) == c