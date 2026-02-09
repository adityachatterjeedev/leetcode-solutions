# Last updated: 2/8/2026, 9:38:13 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        n = len(nums)
5        res = []
6        a = 0
7
8        while a < n - 3:
9            x = nums[a]
10
11            # Early termination: smallest possible sum > target
12            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
13                break
14
15            # Skip if largest possible sum is still too small
16            if x + nums[-1] + nums[-2] + nums[-3] < target:
17                a += 1
18                while a < n - 3 and nums[a] == nums[a - 1]:
19                    a += 1
20                continue
21
22            b = a + 1
23            while b < n - 2:
24                y = nums[b]
25
26                # Early termination on second index
27                if x + y + nums[b + 1] + nums[b + 2] > target:
28                    break
29                if x + y + nums[-1] + nums[-2] < target:
30                    b += 1
31                    while b < n - 2 and nums[b] == nums[b - 1]:
32                        b += 1
33                    continue
34
35                c = b + 1
36                d = n - 1
37                while c < d:
38                    s = x + y + nums[c] + nums[d]
39                    if s < target:
40                        c += 1
41                    elif s > target:
42                        d -= 1
43                    else:
44                        res.append([x, y, nums[c], nums[d]])
45                        c += 1
46                        while c < d and nums[c] == nums[c - 1]:
47                            c += 1
48                        d -= 1
49                        while c < d and nums[d] == nums[d + 1]:
50                            d -= 1
51
52                b += 1
53                while b < n - 2 and nums[b] == nums[b - 1]:
54                    b += 1
55
56            a += 1
57            while a < n - 3 and nums[a] == nums[a - 1]:
58                a += 1
59
60        return res