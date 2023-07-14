class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if i != max(nums) and i != min(nums):
                return i

        return -1
