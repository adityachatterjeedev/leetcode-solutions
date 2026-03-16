# Last updated: 3/15/2026, 8:17:48 PM
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
12
13        for _ in range(n - 1):
14            front = front.next
15
16        back = head
17        prev = None
18
19        while front.next:
20            prev = back
21            back = back.next
22            front = front.next
23        
24        if not prev:
25            head = head.next
26        else:
27            prev.next = back.next
28            back.next = None
29
30        return head    