# Last updated: 7/7/2026, 6:36:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0

            left, right = node.left, node.right

            left_len = dfs(left)
            right_len = dfs(right)

            left_path = right_path = 0

            if left and left.val == node.val:
                left_path = left_len + 1

            if right and right.val == node.val:
                right_path = right_len + 1

            max_path = max(max_path, left_path + right_path)

            return max(left_path, right_path)

        dfs(root)
        return max_path