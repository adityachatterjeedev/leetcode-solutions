# Last updated: 4/3/2026, 12:56:55 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        max_path_sum = float('-inf')
10
11        def dfs(root):
12            nonlocal max_path_sum
13            if not root:
14                return 0
15
16            left = max(dfs(root.left), 0)
17            right = max(dfs(root.right), 0)
18
19            max_path_sum = max(max_path_sum, root.val + left + right)
20
21            return root.val + max(left, right)
22
23        dfs(root)
24
25        return max_path_sum
26        