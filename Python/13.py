class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

        total_sum = 0

        for i in range(len(s)-1):

            if roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                total_sum -= roman_numerals[s[i]]
            else:
                total_sum += roman_numerals[s[i]]
        
        total_sum += roman_numerals[s[-1]]

        return total_sum

