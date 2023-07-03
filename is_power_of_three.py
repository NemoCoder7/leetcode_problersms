import math
import sys


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        max_power = int(math.log(sys.maxsize, 3))
        max_power_of_three = 3 ** max_power

        return max_power_of_three % n == 0
