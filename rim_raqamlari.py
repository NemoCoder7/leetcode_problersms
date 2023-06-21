class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum(roman_dict[s[i]] if roman_dict[s[i]] >= roman_dict[s[i + 1]] else -roman_dict[s[i]] for i in range(len(s) - 1)) + roman_dict[s[-1]]