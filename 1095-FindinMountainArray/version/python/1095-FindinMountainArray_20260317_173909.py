# Last updated: 3/17/2026, 5:39:09 PM
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
22        l, r = 1, mountainArr.length() - 2
23        partition = 0
24        while l <= r:
25            mid = (l + r) // 2
26            left, center, right = cached_get(mid - 1), cached_get(mid), cached_get(mid + 1)
27            if left < center < right:
28                l = mid + 1
29            elif left > center > right:
30                r = mid - 1
31            else:
32                partition = mid
33                break
34
35        #search left
36        l, r= 0, partition
37        while l <= r:
38            mid = (l + r) // 2
39            guess = cached_get(mid)
40            if guess == target:
41                return mid
42            elif guess < target:
43                l = mid + 1
44            else:
45                r = mid - 1
46        
47        #search right
48        l, r = partition + 1, mountainArr.length() - 1
49        while l <= r:
50            mid = (l + r) // 2
51            guess = cached_get(mid)
52            if guess == target:
53                return mid
54            elif guess > target:
55                l = mid + 1
56            else:
57                r = mid - 1
58
59        return -1    