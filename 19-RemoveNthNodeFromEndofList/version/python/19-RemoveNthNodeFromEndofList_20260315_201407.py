# Last updated: 3/15/2026, 8:14:07 PM
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
14        while count < n - 1:
15            front = front.next
16            count += 1
17
18        back = head
19        prev = None
20
21        while front.next:
22            prev = back
23            back = back.next
24            front = front.next
25        
26        if not prev:
27            head = head.next
28        else:
29            prev.next = back.next
30            back.next = None
31
32        return head    