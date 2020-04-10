from typing import List


class Solution:
    @staticmethod
    def letterCombinations(digits: str) -> List[str]:
        dirs = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        res = ['']
        for k in digits:
            res = [i + j for i in res for j in dirs[k]]
        return res
