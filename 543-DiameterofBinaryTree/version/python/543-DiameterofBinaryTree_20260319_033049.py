# Last updated: 3/19/2026, 3:30:49 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11
12        res = 0
13
14        def dfs(root):
15            if not root:
16                return 0
17            nonlocal res
18
19            left = dfs(root.left)
20            right = dfs(root.right)
21            res = max(res, left + right)
22
23            return 1 + max(left,right) # maxHeight
24
25        dfs(root)
26        return res   