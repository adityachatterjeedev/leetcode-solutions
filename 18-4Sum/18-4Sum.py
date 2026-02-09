# Last updated: 2/8/2026, 9:54:51 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        
4        nums.sort()
5        res = []
6        length = len(nums)
7        for a in range(length - 3):
8
9            if a > 0 and nums[a] == nums[a - 1]:
10                continue
11            num_a = nums[a]
12            if num_a + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
13                break
14            if num_a + nums[-1] + nums[-2] + nums[-3] < target:
15                continue
16
17            for b in range(a + 1, length - 2):
18                if b > a + 1 and nums[b] == nums[b - 1]:
19                    continue
20                num_b = nums[b]
21                if num_a + num_b + nums[b + 1] + nums[b + 2] > target:
22                    break
23                if num_a + num_b + nums[-1] + nums[-2] < target:
24                    continue
25
26                left, right = b + 1, length - 1
27                goal = target - (num_a + num_b)
28                while left < right:
29                    if nums[left] + nums[right] == goal:
30                        l_num, r_num = nums[left], nums[right]
31                        res.append([num_a, num_b, l_num, r_num])
32                        while left < right and nums[left] == l_num:
33                            left += 1
34                        while left < right and nums[right] == r_num:
35                            right -= 1
36                    elif nums[left] + nums[right] < goal:
37                        l_num = nums[left]
38                        while left < right and nums[left] == l_num:
39                            left += 1
40                    else:
41                        r_num = nums[right]
42                        while right > left and nums[right] == r_num:
43                            right -= 1
44
45        return res