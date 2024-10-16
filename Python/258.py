class Solution:
    def addDigits(self, num: int) -> int:
        
        if len(str(num))<2:
            return num
        
        num = sum([int(i) for i in str(num)])
        
        return self.addDigits(num)
       