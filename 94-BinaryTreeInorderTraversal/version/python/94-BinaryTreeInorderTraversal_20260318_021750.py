# Last updated: 3/18/2026, 2:17:50 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        if root is None:
10            return []
11        
12        stack = []
13        res = []
14        curr = root
15
16        while curr or stack:
17
18            while curr:
19                stack.append(curr)
20                curr = curr.left
21            
22            curr = stack.pop()
23            res.append(curr.val)
24
25            curr = curr.right
26
27        return res