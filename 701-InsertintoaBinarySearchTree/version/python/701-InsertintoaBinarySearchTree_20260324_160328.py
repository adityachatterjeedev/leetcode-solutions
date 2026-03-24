# Last updated: 3/24/2026, 4:03:28 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        
10        new_node = TreeNode(val = val)
11        if not root:
12            return new_node
13        
14        curr = root
15        prev = None
16        while curr:
17            prev = curr
18            if val <= curr.val:
19                curr = curr.left
20            else:
21                curr = curr.right
22
23        if val <= prev.val:
24            prev.left = new_node
25        else:
26            prev.right = new_node
27        
28        return root 