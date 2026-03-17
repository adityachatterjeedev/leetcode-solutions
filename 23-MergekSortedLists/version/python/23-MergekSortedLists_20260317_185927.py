# Last updated: 3/17/2026, 6:59:27 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        heap = []
9
10        for node in lists:
11            if node:
12                heapq.heappush(heap, (node.val, id(node), node))
13
14        dummy = ListNode()
15        curr = dummy
16
17        while heap:
18            _, _, node = heapq.heappop(heap)
19            
20            curr.next = node
21            curr = node
22            
23            if node.next:
24                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
25
26        return dummy.next