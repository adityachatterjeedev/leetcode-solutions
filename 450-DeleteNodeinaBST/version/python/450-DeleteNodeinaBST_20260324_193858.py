# Last updated: 3/24/2026, 7:38:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
9        
10        def getSuccessor(curr):
11            curr = curr.right
12            while curr and curr.left:
13                curr = curr.left
14            return curr
15        
16        if not root:
17            return
18
19        if key < root.val:
20            root.left = self.deleteNode(root.left, key)
21        elif key > root.val:
22            root.right = self.deleteNode(root.right, key)
23        else:
24            if not root.left:
25                return root.right
26            elif not root.right:
27                return root.left
28            else:
29                curr = root.right
30                while curr.left:
31                    curr = curr.left
32                root.val = curr.val
33                root.right = self.deleteNode(root.right, root.val)
34        
35        return root       