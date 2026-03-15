# Last updated: 3/15/2026, 5:01:55 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        
4        heap = []
5        res = []
6        for i,num in enumerate(nums):
7            heapq.heappush(heap, (-num, i))
8
9            if i >= k - 1:
10                while heap[0][1] <= i - k:
11                    heapq.heappop(heap)
12                res.append(-heap[0][0])
13        
14        return res