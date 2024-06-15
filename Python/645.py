class Solution(object):
    def findErrorNums(self, nums):
        a , b = 0, 0
        l = Counter(nums)
        n = len(nums)
        for i in range(1, n+1):
            if i not in l:
                a = i
            if l[i] > 1:
                b = i

        return[b,a]