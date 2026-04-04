# Last updated: 4/4/2026, 4:48:15 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        count = 0
10        def dfs(root, max_val):
11            nonlocal count
12            if root.val >= max_val:
13                count += 1
14                max_val = root.val
15
16            if root.left:
17                dfs(root.left, max_val)
18            if root.right:
19                dfs(root.right, max_val)
20        
21        dfs(root, root.val - 1)
22        return count