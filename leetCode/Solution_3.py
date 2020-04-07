class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        length, j = 0, -1
        for i, x in enumerate(s):
            if x in s[j + 1:i]:
                length = max(length, i - j - 1)
                j = s[j + 1:i].index(x) + j + 1
        return max(length, len(s) - 1 - j)
