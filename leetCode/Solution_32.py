class Solution:
    @staticmethod
    def longestValidParentheses(s: str) -> int:
        maxNum = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                if stack:
                    maxNum = max(maxNum, i - stack[-1])
        return maxNum
