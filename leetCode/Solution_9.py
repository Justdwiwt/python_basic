class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        return True if str(x) == str(x)[::-1] else False
