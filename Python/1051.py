class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        expected = sorted(heights)
        counter = 0
        for index in range(len(expected)):
            if expected[index]!=heights[index]:
                counter += 1
                
        return counter
