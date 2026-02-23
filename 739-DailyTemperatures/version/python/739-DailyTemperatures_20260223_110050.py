# Last updated: 2/23/2026, 11:00:50 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res =[0] * len(temperatures)
4
5        stack = []
6
7        for i, t in enumerate(temperatures):
8            while stack and stack[-1][0] < t:
9                stackTemp, stackInd = stack.pop()
10                res[stackInd] = (i - stackInd)
11
12            stack.append((t, i))
13
14        return res