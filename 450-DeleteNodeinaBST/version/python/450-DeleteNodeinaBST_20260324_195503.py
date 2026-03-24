# Last updated: 3/24/2026, 7:55:03 PM
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
11            return None
12
13        curr = root
14        parent = None
15        while True:
16            if not curr:
17                return root
18            elif curr.val == key:
19                break
20            else:
21                parent = curr
22                if key < curr.val:
23                    curr = curr.left
24                else:
25                    curr = curr.right
26
27        if not curr.right:
28            if not curr.left: #leaf node
29                if not parent:
30                    return None
31                else:
32                    if curr.val < parent.val:
33                        parent.left = None
34                    else:
35                        parent.right = None
36                    return root
37            else:
38                # only left tree, no right tree
39                if not parent:
40                    return curr.left
41                elif curr.val < parent.val:
42                    parent.left = curr.left
43                else:
44                    parent.right = curr.left
45                return root
46        elif not curr.left:
47            # only right tree, no left tree
48            if not parent:
49                return curr.right
50            elif curr.val < parent.val:
51                parent.left = curr.right
52            else:
53                parent.right = curr.right
54            return root
55        else:
56            succ = curr.right
57            succ_parent = curr
58            while succ.left:
59                succ_parent = succ
60                succ = succ.left
61            curr.val = succ.val
62            if succ_parent == curr:
63                curr.right = succ.right
64            else:
65                succ_parent.left = succ.right
66            return root