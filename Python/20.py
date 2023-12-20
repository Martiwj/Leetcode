class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets and stack:
                
                top = stack.pop()
                if brackets[char] != top:
                    return False

            else:
                stack.append(char)

        
        return not stack 