# Last updated: 4/3/2026, 6:01:24 PM
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
16            left, right = node.left, node.right
17
18            left_len = dfs(left)
19            right_len = dfs(right)
20
21            left_path = right_path = 0
22
23            if left and left.val == node.val:
24                left_path = left_len + 1
25
26            if right and right.val == node.val:
27                right_path = right_len + 1
28
29            max_path = max(max_path, left_path + right_path)
30
31            return max(left_path, right_path)
32
33        dfs(root)
34        return max_path