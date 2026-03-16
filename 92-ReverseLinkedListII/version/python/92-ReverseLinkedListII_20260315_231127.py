# Last updated: 3/15/2026, 11:11:27 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8        if not head.next or left == right:
9            return head
10
11        prev = None
12        curr = head
13        for _ in range(left - 1):
14            prev = curr
15            curr = curr.next
16        
17        l_prev = prev # end of the first part of the unreversed sublist
18                      # prev node for the start of the reversed sublist
19        r_end = curr # end of the reversed sublist
20
21        # reverse sublist
22        prev = curr
23        curr = curr.next
24
25        for _ in range(right - left):
26            nxt = curr.next
27            curr.next = prev
28            prev = curr
29            curr = nxt
30            if nxt:
31                nxt = nxt.next
32
33        # Rewire connections
34        # prev now points to the starting node of the reversed sublist
35        # curr now points to the start of the remaining un-reversed sublist
36        if l_prev:
37            l_prev.next = prev
38        r_end.next = curr 
39
40        if left == 1:
41            return prev
42        else:
43            return head