# Last updated: 3/26/2026, 12:55:25 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        node_stack = [root]
10        max_stack = [float('-inf')]
11        res = 0
12
13        while node_stack:
14            curr = node_stack.pop()
15            high = max_stack.pop()
16
17            val = curr.val
18            if val >= high:
19                res += 1
20                high = val
21
22            left = curr.left
23            right = curr.right
24
25            if right:
26                node_stack.append(right)
27                max_stack.append(high)
28            if left:
29                node_stack.append(left)
30                max_stack.append(high)
31
32        return res