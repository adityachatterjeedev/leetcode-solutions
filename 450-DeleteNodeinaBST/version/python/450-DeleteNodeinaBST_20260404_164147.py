# Last updated: 4/4/2026, 4:41:47 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
9        # stage 1: search
10        prev, curr = None, root
11        while curr:
12            if curr.val == key:
13                break
14            prev = curr
15            if key < curr.val:
16                curr = curr.left
17            else:
18                curr = curr.right
19
20        if curr: # found the key
21            if not curr.left and not curr.right:
22                if not prev:
23                    return None
24                else:
25                    if curr.val < prev.val:
26                        prev.left = None
27                    else:
28                        prev.right = None
29            elif not curr.left:
30                if not prev:
31                    return curr.right
32                else:
33                    if curr.val < prev.val:
34                        prev.left = curr.right
35                    else:
36                        prev.right = curr.right
37                    return root
38            elif not curr.right:
39                if not prev:
40                    return curr.left
41                else:
42                    if curr.val < prev.val:
43                        prev.left = curr.left
44                    else:
45                        prev.right = curr.left
46                    return root
47            else:
48                prev, node = curr, curr.right
49                while node.left:
50                    prev = node
51                    node = node.left
52                curr.val = node.val
53                if node.val < prev.val:
54                    prev.left = node.right
55                else:
56                    prev.right = node.right
57
58        return root
59