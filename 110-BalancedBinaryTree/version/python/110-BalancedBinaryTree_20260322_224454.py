# Last updated: 3/22/2026, 10:44:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        
10        heights = {None : 0}
11
12        stack = []
13        curr = root
14
15        while curr or stack:
16            while curr:
17                stack.append((curr, False))
18                curr = curr.left
19            
20            node, visited = stack.pop()
21
22            if visited:
23                l_height, r_height = heights[node.left], heights[node.right]
24                if abs(l_height - r_height) > 1:
25                    return False
26                heights[node] = 1 + max(l_height, r_height)
27            else:
28                stack.append((node, True))
29                curr = node.right
30        
31        return True
32