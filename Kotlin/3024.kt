class Solution {
    fun triangleType(nums: IntArray): String =
    when{
        nums[0] + nums[1] <= nums[2] || nums[1] + nums[2] <= nums[0] || nums[0] + nums[2] <= nums[1] -> "none"
        nums[0] == nums[1] && nums[1] == nums[2] -> "equilateral"
        nums [0] != nums[1] && nums[1] != nums[2] && nums[2] != nums[0] -> "scalene"
        else -> {
            "isosceles"
        }

    }
}