import re
def isPalindrome(s):
      
    pattern = r'[^a-zA-Z0-9]'
    clean_string = re.sub(pattern, '', s).lower()
    # Alternstive løsning
    # return clean_string == clean_string[::-1]
    left = 0
    right = len(clean_string)-1
    
    while left <= right:
        if clean_string[left] != clean_string[right]:
            return False
        
        left+=1
        right -=1
            
    return True
