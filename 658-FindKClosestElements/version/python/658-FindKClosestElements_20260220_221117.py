# Last updated: 2/20/2026, 10:11:17 PM
1class Solution:
2    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
3        if x <= arr[0]:
4            return arr[:k]
5        if x >= arr[-1]:
6            return arr[-k:]
7        
8        l, r = 0, len(arr) - k
9
10        while l < r:
11            m = (l + r) // 2
12            if (x - arr[m]) > (arr[m + k] - x):
13                l = m + 1
14            else:
15                r = m
16
17        return arr[l:l + k]
18        