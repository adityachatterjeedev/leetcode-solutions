# Last updated: 3/18/2026, 2:30:03 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        if not root:
11            return []
12
13        stack = [root]
14        res = []
15
16        while stack:
17            curr = stack.pop()
18            res.append(curr.val)
19
20            if curr.left:
21                stack.append(curr.left)
22            if curr.right:
23                stack.append(curr.right)
24        
25        res.reverse()
26        return res