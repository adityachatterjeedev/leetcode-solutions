# Last updated: 3/16/2026, 1:58:38 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:    
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        heap = []
9
10        res = ListNode()
11        curr = res
12
13        for i, lst in enumerate(lists):
14            if lst:
15                heapq.heappush(heap, (lst.val, i))
16            
17        while heap:
18            _, ind = heapq.heappop(heap)
19            node = lists[ind]
20            curr.next = lists[ind]
21            curr = lists[ind]
22            lists[ind] = lists[ind].next
23            if lists[ind]:
24                heapq.heappush(heap, (lists[ind].val, ind))
25
26        return res.next