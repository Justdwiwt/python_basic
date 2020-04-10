class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        dirs = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dirs:
                stack.append(c)
            elif dirs[stack.pop()] != c:
                return False
        return len(stack) == 1
