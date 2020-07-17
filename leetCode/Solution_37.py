from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.func(board, 0, 0)

    def func(self, board: List[List[str]], i: int, j: int):
        if j <= 8:
            if board[i][j] != ".":
                if i < 8:
                    if self.func(board, i + 1, j):
                        return True
                else:
                    if self.func(board, 0, j + 1):
                        return True
                return False
            for x in range(1, 10):
                if not self.check(board, i, j, str(x)):
                    continue
                board[i][j] = str(x)
                if i < 8:
                    if self.func(board, i + 1, j):
                        return True
                else:
                    if self.func(board, 0, j + 1):
                        return True
                board[i][j] = '.'
            return False
        return True

    @staticmethod
    def check(board: List[List[str]], i: int, j: int, x: str) -> bool:
        for t in range(9):
            if board[t][j] == x:
                return False
            if board[i][t] == x:
                return False
            if board[i // 3 * 3 + t // 3][j // 3 * 3 + t % 3] == x:
                return False
        return True
