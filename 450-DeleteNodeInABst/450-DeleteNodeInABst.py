# Last updated: 7/7/2026, 6:36:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # stage 1: search
        prev, curr = None, root
        while curr:
            if curr.val == key:
                break
            prev = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if curr: # found the key
            if not curr.left and not curr.right:
                if not prev:
                    return None
                else:
                    if curr.val < prev.val:
                        prev.left = None
                    else:
                        prev.right = None
            elif not curr.left:
                if not prev:
                    return curr.right
                else:
                    if curr.val < prev.val:
                        prev.left = curr.right
                    else:
                        prev.right = curr.right
                    return root
            elif not curr.right:
                if not prev:
                    return curr.left
                else:
                    if curr.val < prev.val:
                        prev.left = curr.left
                    else:
                        prev.right = curr.left
                    return root
            else:
                prev, node = curr, curr.right
                while node.left:
                    prev = node
                    node = node.left
                curr.val = node.val
                if node.val < prev.val:
                    prev.left = node.right
                else:
                    prev.right = node.right

        return root
