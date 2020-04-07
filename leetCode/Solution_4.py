from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length % 2 == 1:
            return nums1[length // 2]
        else:
            return (nums1[length // 2] + nums1[length // 2 - 1]) / 2
