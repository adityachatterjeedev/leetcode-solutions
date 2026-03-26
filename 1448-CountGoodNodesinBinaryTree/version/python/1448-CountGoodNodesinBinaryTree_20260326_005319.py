# Last updated: 3/26/2026, 12:53:19 AM
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
14            good = 0
15            if val >= max_so_far:
16                good = 1
17                max_so_far = val
18
19            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
20
21        return dfs(root, float('-inf'))