# Last updated: 3/22/2026, 10:33:24 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        
10        if not root:
11            return 0
12        heights = {None : 0}
13
14        res = 0
15        stack = []
16        curr = root
17
18        while curr or stack:
19            while curr:
20                stack.append((curr, False))
21                curr = curr.left
22
23            node, visited = stack.pop()
24
25            if not visited:
26                stack.append((node, True))
27                curr = node.right
28            else:
29                res = max(res, heights[node.left] + heights[node.right])
30                heights[node] = 1 + max(heights[node.left], heights[node.right])
31
32        return res   