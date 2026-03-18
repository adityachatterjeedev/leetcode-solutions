# Last updated: 3/18/2026, 2:38:08 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root:
10            return
11
12        stack = [root]
13
14        while stack:
15            curr = stack.pop()
16            curr.left, curr.right = curr.right, curr.left
17            if curr.right:
18                stack.append(curr.right)
19            if curr.left:
20                stack.append(curr.left)
21        
22        return root
23