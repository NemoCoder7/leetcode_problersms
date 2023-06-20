class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_length, left = 0, 0
        char_map = {}

        for right, char in enumerate(s):
            if char in char_map:
                left = max(char_map[char], left)
            longest_length = max(longest_length, right - left + 1)
            char_map[char] = right + 1
        return longest_length