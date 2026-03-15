# Last updated: 3/15/2026, 7:54:28 PM
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
28        second_head = prev
29        
30        p1, p2 = head, second_head
31
32        flag = True
33        while p1 and p2:
34            if flag:
35                p1_nxt = p1.next
36                p1.next = p2
37                p1 = p1_nxt
38                if p1_nxt:
39                    p1_nxt = p1_nxt.next
40            else:
41                p2_nxt = p2.next
42                p2.next = p1
43                p2 = p2_nxt
44                if p2_nxt:
45                    p2_nxt = p2_nxt.next
46            flag = not flag