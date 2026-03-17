# Last updated: 3/17/2026, 5:45:40 PM
1# """
2# This is MountainArray's API interface.
3# You should not implement it, or speculate about its implementation
4# """
5#class MountainArray:
6#    def get(self, index: int) -> int:
7#    def length(self) -> int:
8
9class Solution:
10    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
11        cache = {}
12        
13        def get(i):
14            if i not in cache:
15                cache[i] = mountainArr.get(i)
16            return cache[i]
17        
18        n = mountainArr.length()
19        
20        # 1. Find peak
21        l, r = 0, n - 1
22        while l < r:
23            mid = (l + r) // 2
24            if get(mid) < get(mid + 1):
25                l = mid + 1
26            else:
27                r = mid
28        peak = l
29        
30        # 2. Binary search left (ascending)
31        l, r = 0, peak
32        while l <= r:
33            mid = (l + r) // 2
34            val = get(mid)
35            if val == target:
36                return mid
37            elif val < target:
38                l = mid + 1
39            else:
40                r = mid - 1
41        
42        # 3. Binary search right (descending)
43        l, r = peak + 1, n - 1
44        while l <= r:
45            mid = (l + r) // 2
46            val = get(mid)
47            if val == target:
48                return mid
49            elif val > target:  # reversed comparison
50                l = mid + 1
51            else:
52                r = mid - 1
53        
54        return -1  