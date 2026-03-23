# Last updated: 3/22/2026, 10:59:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        stack = [(p, q)]
10
11        while stack:
12            n1, n2 = stack.pop()
13
14            if not n1 and not n2:
15                continue
16            if not n1 or not n2:
17                return False
18            if n1.val != n2.val:
19                return False
20
21            stack.append((n1.left, n2.left))
22            stack.append((n1.right, n2.right))
23
24        return True     