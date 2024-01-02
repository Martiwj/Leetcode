class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        output = set()
        
        for i, n in enumerate(nums):
            
            if i>0 and n == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
        
            while left < right:
            
                b = nums[left]
                c = nums[right]
                
                total = n + b + c
                
                if total == 0:
                    output.add((n,b,c))
                    
                    left += 1
                    right -= 1
                    
                elif (n + b + c) > 0:
                    right -= 1
                    
                else:
                    left += 1
                    
        
        return list(output)
                    
                    