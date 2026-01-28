# Last updated: 1/28/2026, 2:42:42 AM
1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        
4        def fill(image, row, col, target, color, visited):
5            if image[row][col] == target and (not visited[row][col]):
6                image[row][col] = color
7                visited[row][col] = True
8                if row > 0:
9                    fill(image, row - 1, col, target, color, visited)
10                if col > 0:
11                    fill(image, row, col - 1, target, color, visited)
12                if row < len(image) - 1:
13                    fill(image, row + 1, col, target, color, visited)
14                if col < len(image[0]) - 1:
15                    fill(image, row, col + 1, target, color, visited)
16
17        targetColor = image[sr][sc]
18        visited = [([False] * len(image[0])) for _ in range(len(image))]
19
20        fill(image, sr, sc, targetColor, color, visited)
21
22        return image