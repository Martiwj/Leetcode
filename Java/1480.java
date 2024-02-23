class Solution {
    public int[] runningSum(int[] nums) {

        int[] new_array = new int[nums.length]; 

        int sum = 0; 

        for(int i = 0; i < new_array.length; i++ ){

            sum += nums[i]; 
            new_array[i] = sum; 

        }

        return new_array; 
        
    }
}