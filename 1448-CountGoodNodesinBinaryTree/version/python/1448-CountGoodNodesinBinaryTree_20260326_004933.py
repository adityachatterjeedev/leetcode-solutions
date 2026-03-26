# Last updated: 3/26/2026, 12:49:33 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        stack = [(root, float('-inf'))]
10        res = 0
11
12        while stack:
13            curr, high = stack.pop()
14            if curr.val >= high:
15                res += 1
16                high = curr.val
17            if curr.right:
18                stack.append((curr.right, high))
19            if curr.left:
20                stack.append((curr.left, high))
21
22        return res