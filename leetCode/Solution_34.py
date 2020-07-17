from typing import List


class Solution:
    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            l = left
        elif nums[right] == target:
            l = right
        else:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) >> 1
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            r = right
        elif nums[left] == target:
            r = left
        else:
            return [-1, -1]
        return [l, r]
