# Last updated: 3/15/2026, 11:04:29 PM
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
17        l_prev = prev
18        r_end = curr
19
20        prev = curr
21        curr = curr.next
22
23        for _ in range(right - left):
24            nxt = curr.next
25            curr.next = prev
26            prev = curr
27            curr = nxt
28            if nxt:
29                nxt = nxt.next
30
31        if l_prev:
32            l_prev.next = prev
33        r_end.next = curr
34
35        if left == 1:
36            return prev
37        else:
38            return head