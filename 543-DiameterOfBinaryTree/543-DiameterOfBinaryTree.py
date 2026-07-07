# Last updated: 7/7/2026, 6:36:18 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        heights = {None : 0}

        res = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append((curr, False))
                curr = curr.left

            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))
                curr = node.right
            else:
                l_height, r_height = heights[node.left], heights[node.right]
                res = max(res, l_height + r_height)
                heights[node] = 1 + max(l_height, r_height)

        return res   