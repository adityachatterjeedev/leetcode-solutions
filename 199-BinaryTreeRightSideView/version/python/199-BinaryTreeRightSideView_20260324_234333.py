# Last updated: 3/24/2026, 11:43:33 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if not root:
10            return []
11        q = deque()
12        q.append(root)
13        res = []
14
15        while q:
16            size = len(q)
17            count = 0
18            curr = None
19            while count < size:
20                curr = q.pop()
21
22                if curr.left:
23                    q.appendleft(curr.left)
24                if curr.right:
25                    q.appendleft(curr.right)
26                count += 1
27                
28            res.append(curr.val)
29        
30        return res     