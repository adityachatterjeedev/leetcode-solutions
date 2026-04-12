# Last updated: 4/12/2026, 12:56:52 PM
1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3        res = []
4
5        curr = []
6
7        def combo(i, rem):
8            if rem == 0:
9                res.append(curr[:])
10                return
11            
12            for j in range(i, n):
13                curr.append(j + 1)
14                combo(j + 1, rem - 1)
15                curr.pop()
16        
17        combo(0, k)
18        return res