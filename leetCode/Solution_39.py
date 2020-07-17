from typing import List


class Solution:
    @staticmethod
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(temp, res):
            nonlocal target
            if temp > target:
                return
            if temp == target:
                ans.append(res[:])
                return
            for i in candidates:
                if res and res[-1] > i:
                    continue
                dfs(temp + i, res + [i])

        dfs(0, [])
        return ans
