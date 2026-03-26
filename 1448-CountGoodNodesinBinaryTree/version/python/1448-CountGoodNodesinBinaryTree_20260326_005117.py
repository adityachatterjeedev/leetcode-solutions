# Last updated: 3/26/2026, 12:51:17 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        def dfs(node, max_so_far):
10            if not node:
11                return 0
12            
13            val = node.val
14            good = 1 if val >= max_so_far else 0
15            max_so_far = max(max_so_far, val)
16
17            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
18
19        return dfs(root, float('-inf'))