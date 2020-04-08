import re


class Solution:
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        return True if re.match(p + '$', s) else False
