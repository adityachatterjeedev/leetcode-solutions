# Last updated: 7/31/2025, 5:08:40 PM
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]
                self.sumMat[row + 1][col + 1] = prefix + self.sumMat[row][col + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1 ,row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sumMat[row2][col2] - self.sumMat[row1 - 1][col2] - self.sumMat[row2][col1 - 1] + self.sumMat[row1 - 1][col1 - 1]