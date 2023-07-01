class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sl = sorted([i for i in s])
        tl = sorted([i for i in t])
        return sl == tl
