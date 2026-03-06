# Last updated: 3/5/2026, 10:12:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        
10        def balancedTree(root):
11            if not root:
12                return (True, 0)
13            
14            (f1, h1) = balancedTree(root.left)
15            (f2, h2) = balancedTree(root.right)
16
17            return (((f1 and f2) and abs(h2 - h1) <= 1), 1 + max(h1,h2))
18
19        return balancedTree(root)[0]
20