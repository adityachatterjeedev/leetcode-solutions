# Last updated: 1/28/2026, 2:21:51 AM
1class NumMatrix:
2
3    def __init__(self, matrix: List[List[int]]):
4        ROWS, COLS = len(matrix), len(matrix[0])
5        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
6
7        for row in range(ROWS):
8            prefix = 0
9            for col in range(COLS):
10                prefix += matrix[row][col]
11                self.sumMat[row + 1][col + 1] = prefix + self.sumMat[row][col + 1]
12
13    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
14        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
15
16        return self.sumMat[row2][col2] + self.sumMat[row1 - 1][col1 - 1] - self.sumMat[row1 -1][col2] - self.sumMat[row2][col1 - 1]