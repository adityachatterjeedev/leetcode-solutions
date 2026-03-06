# Last updated: 3/5/2026, 7:27:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        (val1, val2) = (p.val,q.val) if p.val <= q.val else (q.val,p.val)
11        curr = root
12        while not (val1 <= curr.val and curr.val <= val2):
13            if val1 < curr.val:
14                curr = curr.left
15            else:
16                curr = curr.right
17        return curr