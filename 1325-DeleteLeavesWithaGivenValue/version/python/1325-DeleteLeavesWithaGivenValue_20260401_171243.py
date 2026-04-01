# Last updated: 4/1/2026, 5:12:43 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
9        
10        def remove(root):
11            if root.left and remove(root.left):
12                root.left = None
13            if root.right and remove(root.right):
14                root.right = None
15            
16            if (not root.left) and (not root.right) and root.val == target:
17                return True
18            return False
19
20        return None if remove(root) else root       