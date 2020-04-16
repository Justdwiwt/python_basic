from typing import List


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        mx = dict()
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp in mx.keys():
                mx[tmp].append(i)
            else:
                mx[tmp] = [i]
        return list(mx.values())
