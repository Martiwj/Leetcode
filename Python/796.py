from collections import deque
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        string_arr = deque(list(s))
        n = len(s)
        res = s
        for _ in range(n):
            if res == goal:
                return True
            shift = string_arr.popleft()
            string_arr.append(shift)
            res = "".join(string_arr)
            
        return False