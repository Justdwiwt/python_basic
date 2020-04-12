from typing import List


class Solution:
    @staticmethod
    def findSubstring(s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        wordLen = len(words[0])
        wordNum = len(words)
        allLen = wordLen * wordNum
        harsh = Counter(words)
        n = len(s)
        index = []
        for i in range(0, n - allLen + 1):
            a = []
            for j in range(i, i + allLen, wordLen):
                a.append(s[j:j + wordLen])
            res = Counter(a)
            if res == harsh:
                index.append(i)
        return index
