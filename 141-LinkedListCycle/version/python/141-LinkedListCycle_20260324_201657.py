# Last updated: 3/24/2026, 8:16:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if not head:
10            return False
11        
12        slow = fast = head
13
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17
18            if slow == fast:
19                return True
20
21        return False