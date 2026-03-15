# Last updated: 3/15/2026, 7:58:19 PM
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
30        second = prev
31        first = head
32
33        # Step 3: merge
34        while second:
35            tmp1 = first.next
36            tmp2 = second.next
37
38            first.next = second
39            second.next = tmp1
40
41            first = tmp1
42            second = tmp2