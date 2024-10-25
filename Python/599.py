class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        
        seen = {}
        
        for i , (z, j) in enumerate(zip(list1, list2)):
            
            