# Last updated: 4/3/2026, 5:57:36 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        
12        max_path_len = 0
13        
14        def dfs(root):
15            nonlocal max_path_len
16            l, r = 0,0
17            if root.left:
18                l = dfs(root.left)
19                if root.left.val != root.val:
20                    l = 0
21
22            if root.right:
23                r = dfs(root.right)
24                if root.right.val != root.val:
25                    r = 0
26
27            max_path_len = max(max_path_len, 1 + l + r)
28
29            return 1 + max(l, r)
30
31        dfs(root)
32
33        return max_path_len - 1