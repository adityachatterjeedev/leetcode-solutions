# Last updated: 3/17/2026, 5:43:33 PM
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
11        
12        cache = {}
13
14        def cached_get(index):
15            if index in cache:
16                return cache[index]
17            val = mountainArr.get(index)
18            cache[index] = val
19            return val
20
21        # find partition
22        l, r = 0, mountainArr.length() - 1
23        while l < r:
24            mid = (l + r) // 2
25            if cached_get(mid) < cached_get(mid + 1):
26                l = mid + 1
27            else:
28                r = mid
29        partition = l
30
31        #search left
32        l, r= 0, partition
33        while l <= r:
34            mid = (l + r) // 2
35            guess = cached_get(mid)
36            if guess == target:
37                return mid
38            elif guess < target:
39                l = mid + 1
40            else:
41                r = mid - 1
42        
43        #search right
44        l, r = partition + 1, mountainArr.length() - 1
45        while l <= r:
46            mid = (l + r) // 2
47            guess = cached_get(mid)
48            if guess == target:
49                return mid
50            elif guess > target:
51                l = mid + 1
52            else:
53                r = mid - 1
54
55        return -1    