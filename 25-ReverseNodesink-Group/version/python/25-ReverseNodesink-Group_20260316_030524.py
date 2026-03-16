# Last updated: 3/16/2026, 3:05:24 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
9    # ONE PASS 
10        if not head:
11            return None
12        
13        right = head
14
15        prev = None
16        curr = head
17        l_prev = None
18        r_end = None
19        while True:
20
21            # check if there are at least k more nodes, else return
22            for _ in range(k): 
23                if not right:
24                    return head
25                right = right.next
26            
27            #reverse k nodes
28            l_prev = r_end
29            r_end = curr
30            nxt = curr.next
31            for _ in range(k):
32                curr.next = prev
33                prev = curr
34                curr = nxt
35                if nxt:
36                    nxt = nxt.next
37
38            if l_prev:
39                l_prev.next = prev
40            else:
41                head = prev
42            r_end.next = curr
43
44        return head
45