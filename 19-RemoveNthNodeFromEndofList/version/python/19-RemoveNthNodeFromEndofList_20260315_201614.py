# Last updated: 3/15/2026, 8:16:14 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        if not head.next:
9            return None
10        
11        front = head
12        count = 0
13
14        for _ in range(n - 1):
15            front = front.next
16
17        back = head
18        prev = None
19
20        while front.next:
21            prev = back
22            back = back.next
23            front = front.next
24        
25        if not prev:
26            head = head.next
27        else:
28            prev.next = back.next
29            back.next = None
30
31        return head    