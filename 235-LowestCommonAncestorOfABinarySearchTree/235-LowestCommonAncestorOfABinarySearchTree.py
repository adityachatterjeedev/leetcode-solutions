# Last updated: 7/7/2026, 6:36:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root is p:
            return p
        if root is q:
            return q
        (val1, val2) = (p.val,q.val) if p.val <= q.val else (q.val,p.val)
        curr = root
        while not (val1 <= curr.val and curr.val <= val2):
            if val1 < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr