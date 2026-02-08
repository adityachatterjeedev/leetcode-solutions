# Last updated: 2/8/2026, 3:49:19 AM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def fill(image, row, col, target, color):
            if image[row][col] == target:
                image[row][col] = color
                if row > 0:
                    fill(image, row - 1, col, target, color)
                if col > 0:
                    fill(image, row, col - 1, target, color)
                if row < len(image) - 1:
                    fill(image, row + 1, col, target, color)
                if col < len(image[0]) - 1:
                    fill(image, row, col + 1, target, color)

        targetColor = image[sr][sc]
        if targetColor == color:
            return image

        fill(image, sr, sc, targetColor, color)

        return image