# Last updated: 4/3/2026, 5:37:56 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        if not root:
10            return False
11        
12        if not root.left and not root.right:
13            return root.val == targetSum
14        diff = targetSum - root.val
15        return self.hasPathSum(root.left, diff) or self.hasPathSum(root.right, diff)