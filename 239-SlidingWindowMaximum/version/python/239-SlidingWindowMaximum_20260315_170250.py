# Last updated: 3/15/2026, 5:02:50 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        output = []
4        q = deque()  # index
5        l = r = 0
6
7        while r < len(nums):
8            while q and nums[q[-1]] < nums[r]:
9                q.pop()
10            q.append(r)
11
12            if l > q[0]:
13                q.popleft()
14
15            if (r + 1) >= k:
16                output.append(nums[q[0]])
17                l += 1
18            r += 1
19
20        return output