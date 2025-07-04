# Last updated: 6/16/2025, 3:22:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        elif (root.left is None) and (root.right is None): #leaf node
            return root
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
