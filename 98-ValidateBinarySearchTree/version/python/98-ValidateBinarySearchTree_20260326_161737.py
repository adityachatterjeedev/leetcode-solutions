# Last updated: 3/26/2026, 4:17:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        
10        def validateBST(root, nodemin, nodemax):
11            if not root:
12                return True
13            if root.val <= nodemin or root.val >= nodemax:
14                return False
15            
16            return validateBST(root.left, nodemin, root.val) and validateBST(root.right, root.val, nodemax)
17
18        return validateBST(root, float('-inf'), float('inf'))       