# Last updated: 1/28/2026, 2:20:09 AM
1class NumMatrix:
2
3    def __init__(self, matrix: List[List[int]]):
4        ROWS = len(matrix) + 1
5        COLS = len(matrix[0]) + 1
6        self.prefs = [([0] * COLS) for _ in range(ROWS)]
7        for r in range(ROWS - 1):
8            pref = 0
9            for c in range(COLS - 1):
10                pref += matrix[r][c]
11                self.prefs[r + 1][c + 1] = self.prefs[r][c + 1]  + pref
12
13    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
14        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
15
16        return self.prefs[row2][col2] + self.prefs[row1 - 1][col1 - 1] - self.prefs[row1 -1][col2] - self.prefs[row2][col1 - 1]