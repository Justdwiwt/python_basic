from typing import List


class Solution:
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        if not nums or 0 not in nums:
            nums.append(0)
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            while 0 <= nums[i] < len(nums) and nums[i] != i and nums[i] != nums[nums[i]]:
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp
        for j in range(1, len(nums)):
            if nums[j] != j:
                return j
        return len(nums)
