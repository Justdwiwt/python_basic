from typing import List


class Solution:
    @staticmethod
    def permuteUnique(nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def back(num, tmp):
            if not num:
                res.append(tmp)
                return
            else:
                for i in range(len(num)):
                    if i > 0 and num[i] == num[i - 1]:
                        continue
                    back(num[:i] + num[i + 1:], tmp + [num[i]])

        back(nums, temp)
        return res
