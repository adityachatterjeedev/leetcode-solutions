# Last updated: 3/24/2025, 10:42:01 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        returned = []
        
        if root.left is not None:
            returned += self.inorderTraversal(root.left)
        returned.append(root.val)
        if root.right is not None:
            returned += self.inorderTraversal(root.right)
        
        return returned