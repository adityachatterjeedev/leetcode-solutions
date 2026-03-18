# Last updated: 3/18/2026, 2:45:25 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        else:
12            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))