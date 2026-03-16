# Last updated: 3/15/2026, 8:51:26 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10"""
11# Definition for a Node.
12class Node:
13    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
14        self.val = int(x)
15        self.next = next
16        self.random = random
17"""
18
19class Solution:
20    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
21        if not head:
22            return None
23        node_map = {}
24        curr = head
25        new_prev = None
26        while curr:
27            new_node = Node(curr.val)
28            if new_prev:
29                new_prev.next = new_node
30            new_prev = new_node
31            node_map[curr] = new_node
32            if curr.random in node_map:
33                new_node.random = node_map[curr.random]
34            else:
35                new_node.random = curr.random
36            curr = curr.next
37
38        #second pass
39        curr = node_map[head]
40        while curr:
41            if curr.random in node_map:
42                curr.random = node_map[curr.random]
43            curr = curr.next
44        
45        return node_map[head]