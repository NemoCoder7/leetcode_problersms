class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for num in nums:
            if num != nums[k]:
                k += 1
                nums[k] = num
        return k + 1