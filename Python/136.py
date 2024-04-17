from collections import defaultdict
class Solution(object):
    def singleNumber(self, nums):
        n = defaultdict(int)
        for i in nums:
            n[i]+=1  
        return min(n, key=n.get) 
    
     
