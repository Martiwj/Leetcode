class Solution {
    public boolean isPalindrome(int x) {
        String num = x +""; 
        
        int right = num.length()-1; 
        int left = 0; 

        while (left < right){

            if(num.charAt(left) != num.charAt(right)){
                return false; 
            }
            right --; 
            left ++; 
        }

        return true;  
    }
}