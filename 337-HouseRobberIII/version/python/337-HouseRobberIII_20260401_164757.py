# Last updated: 4/1/2026, 4:47:57 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        
10        #dp[root] = if not robbing root, rob root.left + rob root.right
11        # if robbing root, root.val + rob children of left + rob children of right
12        #i.e root.val + rob(root.left.left + root.left.right + root.right.left + root.right.right)
13
14        dp_table = {}
15        
16        def dfs(root: Optional[TreeNode]) -> int:
17            if not root:
18                return 0
19            if root in dp_table:
20                return dp_table[root]
21            if (not root.left) and (not root.right):
22                dp_table[root] = root.val
23                return root.val
24            
25            rob_left = dfs(root.left)
26            rob_right = dfs(root.right)
27            rob_left_left = dfs(root.left.left) if root.left else 0
28            rob_left_right = dfs(root.left.right) if root.left else 0
29            rob_right_left = dfs(root.right.left) if root.right else 0
30            rob_right_right = dfs(root.right.right) if root.right else 0
31
32            val = max(rob_left + rob_right, root.val + rob_left_left + rob_left_right + rob_right_left + rob_right_right)
33            dp_table[root] = val
34            return val
35        
36        return dfs(root)      