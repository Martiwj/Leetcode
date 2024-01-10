class Solution {

    public int missingNumber(int[] nums) {
        
        int count = 0; 
        for(int i =0; i < nums.length; i++ ){
            count -= nums[i]; 
            count += i +1; 
        }

        return count; 
        
    }
}