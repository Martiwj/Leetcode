class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        
        idx = 0
        
        # Beregn summen av alle elementene i nums én gang
        total_sum = int("".join([num * num for num in nums]))
        
        while (len(output) != len(nums)):
            # Beregn produktet uten nums[idx] ved å bruke total_sum
            output.append(total_sum / nums[idx])
            idx = (idx + 1) % len(nums)
     
        return output
            
            
        