# Last updated: 2/8/2026, 3:25:40 AM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        e1 = 0
5        length = len(nums)
6        result = []
7        while e1 < length - 3:
8            e2 = e1 + 1
9            while e2 < length - 2:
10                goal = target - (nums[e1] + nums[e2])
11                left, right = e2 + 1, length - 1
12                while left < right:
13                    total = nums[left] + nums[right]
14                    if total == goal:
15                        result.append([nums[e1], nums[e2], nums[left], nums[right]])
16                        n = left + 1
17                        while n < right and nums[n] == nums[n - 1]:
18                            n += 1
19                        left = n
20                    elif total < goal:
21                        left += 1
22                    else:
23                        right -= 1
24
25                nxt = e2 + 1
26                while nxt < length - 2 and nums[nxt] == nums[nxt - 1]:
27                    nxt += 1
28                e2 = nxt
29            
30            nextindex = e1 + 1
31            while nextindex < length - 3 and nums[nextindex] == nums[nextindex - 1]:
32                nextindex += 1
33            e1 = nextindex
34
35        return result