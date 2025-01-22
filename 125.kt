class Solution {
    fun isPalindrome(s: String): Boolean {
        val normalizedS = s.filter { it.isLetterOrDigit() }.lowercase()
        return normalizedS == normalizedS.reversed()
    }
}