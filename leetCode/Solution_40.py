from typing import List


class Solution:
    @staticmethod
    def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        n = len(candidates)
        candidates.sort()
        res = []

        def helper(i, tmp, tar):
            if tar == 0:
                res.append(tmp)
                return
            if i == n or tar < candidates[i]:
                return
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                helper(j + 1, tmp + [candidates[j]], tar - candidates[j])

        helper(0, [], target)
        return res
