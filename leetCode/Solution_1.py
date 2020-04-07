from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            if m.get(target - num) is not None:
                return [i, m.get(target - num)]
            m[num] = i
