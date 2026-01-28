# Last updated: 1/28/2026, 2:44:10 AM
1class Solution(object):
2    def floodFill(self, image, sr, sc, color):
3        old = image[sr][sc]
4        if old == color:
5            return image
6        m = len(image)
7        n = len(image[0])
8        def dfs(i, j):
9            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != old:
10                return
11            image[i][j] = color
12            dfs(i + 1, j)
13            dfs(i - 1, j)
14            dfs(i, j + 1)
15            dfs(i, j - 1)
16        dfs(sr, sc)
17        return image