class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x < 0:
            return -1 * int(s[:0:-1])
        else:
            return int(s[::-1])
