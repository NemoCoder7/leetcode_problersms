class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = sorted(nums1 + nums2)
        total_length = len(merged_list)
        middle = total_length // 2

        if total_length % 2 == 0:
            return (merged_list[middle - 1] + merged_list[middle]) / 2.0
        else:
            return merged_list[middle]
