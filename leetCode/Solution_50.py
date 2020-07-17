class Solution:
    @staticmethod
    def myPow(x: float, n: int) -> float:
        judge = True
        if n < 0:
            n = -n
            judge = False
        final = 1
        while n > 0:
            if n & 1:
                final *= x
            x *= x
            n >>= 1
        return final if judge else 1 / final
