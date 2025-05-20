 class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
      
      val seen = mutableMapOf<Int, Int>()

      nums.forEachIndexed{ index, value ->
        val complement = target - value

        seen[complement]?.let { compIndex -> 
          return intArrayOf(compIndex, index)
        }
        seen[value] = index

      }
      return intArrayOf()

    }

  }

