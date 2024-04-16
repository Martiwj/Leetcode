class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        number = str(int("".join(map(str,digits)))+1)
        return [int(n) for n in number]

        
        
        