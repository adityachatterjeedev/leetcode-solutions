# Last updated: 3/26/2026, 4:28:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        
10        stack = []
11        count = 0
12
13        curr = root
14
15        while curr or stack:
16            while curr:
17                stack.append(curr)
18                curr = curr.left
19
20            curr = stack.pop()
21            count += 1
22            if count == k:
23                return curr.val
24
25            curr = curr.right    