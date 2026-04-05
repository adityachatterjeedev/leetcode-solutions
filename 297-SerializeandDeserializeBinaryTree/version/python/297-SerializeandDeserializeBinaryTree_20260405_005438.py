# Last updated: 4/5/2026, 12:54:38 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9    
10    # Encodes a tree to a single string.
11    def serialize(self, root: Optional[TreeNode]) -> str:
12        result = []
13
14        def dfs(node):
15            nonlocal result
16            if not node:
17                result.append('null')
18                return
19            result.append(str(node.val))
20            dfs(node.left)
21            dfs(node.right)
22
23        dfs(root)
24        return ','.join(result)
25        
26    # Decodes your encoded data to tree.
27    def deserialize(self, data: str) -> Optional[TreeNode]:
28        nodes = data.split(',')
29        le = len(nodes)
30        index = -1
31        def des_preorder() -> Optional[TreeNode]:
32            nonlocal index
33            index += 1
34            if index >= le or nodes[index] == 'null':
35                return None
36            node = TreeNode(val = int(nodes[index]))
37            node.left = des_preorder()
38            node.right = des_preorder()
39            return node
40        root = des_preorder()
41        return root
42        
43
44# Your Codec object will be instantiated and called as such:
45# ser = Codec()
46# deser = Codec()
47# ans = deser.deserialize(ser.serialize(root))