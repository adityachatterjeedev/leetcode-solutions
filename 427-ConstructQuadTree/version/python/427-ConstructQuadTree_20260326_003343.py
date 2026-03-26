# Last updated: 3/26/2026, 12:33:43 AM
1"""
2# Definition for a QuadTree node.
3class Node:
4    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
5        self.val = val
6        self.isLeaf = isLeaf
7        self.topLeft = topLeft
8        self.topRight = topRight
9        self.bottomLeft = bottomLeft
10        self.bottomRight = bottomRight
11"""
12
13class Solution:
14    def construct(self, grid: List[List[int]]) -> 'Node':
15        def dfs(n, r, c):
16            if n == 1:
17                return Node(grid[r][c] == 1, True)
18
19            half = n // 2
20            topLeft = dfs(half, r, c)
21            topRight = dfs(half, r, c + half)
22            bottomLeft = dfs(half, r + half, c)
23            bottomRight = dfs(half, r + half, c + half)
24
25            # merge if possible
26            if (topLeft.isLeaf and topRight.isLeaf and
27                bottomLeft.isLeaf and bottomRight.isLeaf and
28                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
29
30                return Node(topLeft.val, True)
31
32            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
33
34        return dfs(len(grid), 0, 0)    