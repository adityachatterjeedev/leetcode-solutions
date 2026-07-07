# Last updated: 7/7/2026, 6:36:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return (0,0)
            
            rob_left = dfs(root.left)
            rob_right = dfs(root.right)

            return (root.val + rob_left[1] + rob_right[1], max(rob_left) + max(rob_right))

        return max(dfs(root))     