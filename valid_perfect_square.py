class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        snum = num ** 0.5
        return snum == int(snum)
