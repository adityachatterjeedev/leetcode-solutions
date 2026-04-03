# Last updated: 4/3/2026, 5:42:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sumNumbers(self, root: Optional[TreeNode]) -> int:
9        total = 0
10
11        def dfs(root, num_str):
12            nonlocal total
13            new_str = num_str + str(root.val)
14            if not root.left and not root.right:
15                total += int(new_str)
16            if root.left:
17                dfs(root.left, new_str)
18            if root.right:
19                dfs(root.right, new_str)
20
21        dfs(root, '')
22        return total