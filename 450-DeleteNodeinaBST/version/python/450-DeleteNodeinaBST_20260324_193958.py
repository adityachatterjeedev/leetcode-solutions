# Last updated: 3/24/2026, 7:39:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
9
10        if not root:
11            return
12
13        if key < root.val:
14            root.left = self.deleteNode(root.left, key)
15        elif key > root.val:
16            root.right = self.deleteNode(root.right, key)
17        else:
18            if not root.left:
19                return root.right
20            elif not root.right:
21                return root.left
22            else:
23                curr = root.right
24                while curr.left:
25                    curr = curr.left
26                root.val = curr.val
27                root.right = self.deleteNode(root.right, root.val)
28        
29        return root       