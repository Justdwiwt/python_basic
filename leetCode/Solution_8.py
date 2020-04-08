import re


class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        return max(min(int(*re.findall('^[+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)
