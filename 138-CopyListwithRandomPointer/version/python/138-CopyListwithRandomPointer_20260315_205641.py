# Last updated: 3/15/2026, 8:56:41 PM
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
23
24        new_head = Node(head.val, next = None, random = head.random)
25        node_map = {head : new_head}
26        curr = head.next
27        new_prev = new_head
28        while curr:
29            new_node = Node(curr.val)
30            new_prev.next = new_node
31            new_prev = new_node
32            node_map[curr] = new_node
33            if curr.random and curr.random in node_map:
34                new_node.random = node_map[curr.random]
35            else:
36                new_node.random = curr.random
37            curr = curr.next
38
39        #second pass
40        curr = new_head
41        while curr:
42            if curr.random and curr.random in node_map:
43                curr.random = node_map[curr.random]
44            curr = curr.next
45        
46        return node_map[head]