# Last updated: 1/28/2026, 2:45:48 AM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        
4        def fill(image, row, col, target, color):
5            if image[row][col] == target:
6                image[row][col] = color
7                if row > 0:
8                    fill(image, row - 1, col, target, color)
9                if col > 0:
10                    fill(image, row, col - 1, target, color)
11                if row < len(image) - 1:
12                    fill(image, row + 1, col, target, color)
13                if col < len(image[0]) - 1:
14                    fill(image, row, col + 1, target, color)
15
16        targetColor = image[sr][sc]
17        if targetColor == color:
18            return image
19
20        fill(image, sr, sc, targetColor, color)
21
22        return image