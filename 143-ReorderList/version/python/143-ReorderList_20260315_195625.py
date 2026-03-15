# Last updated: 3/15/2026, 7:56:25 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        if not head.next:
9            return
10        
11        # find middle
12        slow, fast = head, head
13        while fast and fast.next:
14            slow = slow.next
15            fast = fast.next.next
16
17        # reverse second half
18        prev = None
19        curr = slow.next
20        slow.next = None
21
22        while curr:
23            nxt = curr.next
24            curr.next = prev
25            prev = curr
26            curr = nxt
27        
28        p1, p2 = head, prev
29
30        flag = True
31        while p1 and p2:
32            if flag:
33                p1_nxt = p1.next
34                p1.next = p2
35                p1 = p1_nxt
36                if p1_nxt:
37                    p1_nxt = p1_nxt.next
38            else:
39                p2_nxt = p2.next
40                p2.next = p1
41                p2 = p2_nxt
42                if p2_nxt:
43                    p2_nxt = p2_nxt.next
44            flag = not flag