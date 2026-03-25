# Last updated: 3/24/2026, 11:35:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11
12        q = deque()
13        res = []
14
15        q.append(root)
16
17        while q:
18            size = len(q)
19
20            temp = []
21
22            count = 0
23
24            while count < size:
25                curr = q.pop()
26                temp.append(curr.val)
27                if curr.left:
28                    q.appendleft(curr.left)
29                if curr.right:
30                    q.appendleft(curr.right)
31                count += 1
32            res.append(temp)
33
34        return res     