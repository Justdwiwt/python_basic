class Solution:
    @staticmethod
    def longestPalindrome(s: str) -> str:
        def expand(l, r):
            while 0 <= l and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        if not s or len(s) == 1:
            return s
        n = len(s)
        start = 0
        end = 0
        for i in range(n):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)
            mx = max(len1, len2)
            if mx > end - start:
                start = i - (mx - 1) // 2
                end = i + mx // 2
        return s[start:end + 1]
