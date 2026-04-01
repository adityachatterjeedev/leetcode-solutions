# Last updated: 4/1/2026, 5:19:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def removeLeafNodes(self, root, target):
9        if not root:
10            return None
11
12        root.left = self.removeLeafNodes(root.left, target)
13        root.right = self.removeLeafNodes(root.right, target)
14
15        if not root.left and not root.right and root.val == target:
16            return None
17
18        return root      