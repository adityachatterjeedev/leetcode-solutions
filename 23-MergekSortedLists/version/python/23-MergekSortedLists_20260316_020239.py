# Last updated: 3/16/2026, 2:02:39 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        heap = []
9        res = ListNode(0)
10        curr = res
11
12        # Initialize heap with (value, index) tuples
13        for i, node in enumerate(lists):
14            if node:
15                heapq.heappush(heap, (node.val, i))
16
17        while heap:
18            val, ind = heapq.heappop(heap)
19            node = lists[ind]          
20            curr.next = node
21            curr = node
22            lists[ind] = node.next     
23            if lists[ind]:
24                heapq.heappush(heap, (lists[ind].val, ind))
25
26        return res.next