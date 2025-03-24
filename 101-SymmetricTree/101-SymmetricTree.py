# Last updated: 3/24/2025, 10:43:19 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def areTwoNodesSymmetric(node1: TreeNode, node2: TreeNode) -> bool:
            if node1 is None and node2 is None:
                return True
            elif (not node1) or (not node2):
                return False
            
            return (node1.val == node2.val) and areTwoNodesSymmetric(node1.left, node2.right) and areTwoNodesSymmetric(node1.right, node2.left)
        if not root:
            return False
        return areTwoNodesSymmetric(root.left, root.right)
        