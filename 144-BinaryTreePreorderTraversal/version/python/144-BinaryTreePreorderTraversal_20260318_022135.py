# Last updated: 3/18/2026, 2:21:35 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        if not root:
11            return []
12
13        stack = [root]
14
15        res = []
16
17        while stack:
18            curr = stack.pop()
19            res.append(curr.val)
20            if curr.right:
21                stack.append(curr.right)
22            if curr.left:
23                stack.append(curr.left)
24
25        return res     