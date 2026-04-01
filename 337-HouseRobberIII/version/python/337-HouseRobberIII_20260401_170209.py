# Last updated: 4/1/2026, 5:02:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9
10        def dfs(root):
11            if not root:
12                return (0,0)
13            
14            rob_left = dfs(root.left)
15            rob_right = dfs(root.right)
16
17            return (root.val + rob_left[1] + rob_right[1], max(rob_left) + max(rob_right))
18
19        return max(dfs(root))     