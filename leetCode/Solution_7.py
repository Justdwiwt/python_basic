class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        num = str(x)[::-1]
        if num.endswith('-'):
            num = '-' + num[:-1]
            return int(num) if int(num) >= -2 ** 31 else 0
        return int(num) if int(num) <= 2 ** 31 - 1 else 0
