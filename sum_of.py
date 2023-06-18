class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        self.nums = nums
        self.target = target

        num_dict = {}  # Use a dictionary to store numbers and their indices

        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

        return []  # Return an empty list if no solution is found


c = Solution()
print(c.twoSum([3, 2, 4], 6))
