impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {

        let mut new_array: Vec<i32> = vec![0; nums.len()];        
        let mut sum: i32 = 0; 

        for i in 0..new_array.len()-1{
             sum += nums[i]
             new_array[i] = sum

        }

        new_array
    }
}