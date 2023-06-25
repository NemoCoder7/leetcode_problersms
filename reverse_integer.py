class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x < 0:
            reversed_str = s[:0:-1]
            reversed_value = -int(reversed_str)
        else:
            reversed_str = s[::-1]
            reversed_value = int(reversed_str)

        if reversed_value < -2 ** 31 or reversed_value > 2 ** 31 - 1:
            return 0
        else:
            return reversed_value
