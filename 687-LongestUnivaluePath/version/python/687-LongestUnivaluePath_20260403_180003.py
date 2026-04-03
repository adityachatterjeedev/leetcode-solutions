# Last updated: 4/3/2026, 6:00:03 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
9        max_path = 0
10
11        def dfs(node):
12            nonlocal max_path
13            if not node:
14                return 0
15
16            left_len = dfs(node.left)
17            right_len = dfs(node.right)
18
19            left_path = right_path = 0
20
21            if node.left and node.left.val == node.val:
22                left_path = left_len + 1
23
24            if node.right and node.right.val == node.val:
25                right_path = right_len + 1
26
27            max_path = max(max_path, left_path + right_path)
28
29            return max(left_path, right_path)
30
31        dfs(root)
32        return max_path