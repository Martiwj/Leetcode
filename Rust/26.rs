impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut j = 0; 

        let vec_length = nums.len(); 

        for i in 1..vec_length{
            if nums[i] != nums[j]{
                j += 1; 
                nums[j] = nums[i];
            
            }
        }
        (j+1) as i32
    }
}