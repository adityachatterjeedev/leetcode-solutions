# Last updated: 2/8/2026, 3:46:37 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        result = []
5        for i, num in enumerate(nums):
6            if num > 0:
7                break
8            if i == 0 or (nums[i - 1] != nums[i]):
9                target = -num
10                l, r = i + 1, len(nums) - 1
11                while l < r:
12                    total = nums[l] + nums[r]
13                    if total < target:
14                        l += 1
15                    elif total > target:
16                        r -= 1
17                    else:
18                        left = nums[l]
19                        result += [[num, left, nums[r]]]
20                        while nums[l] == left and l < r:
21                            l += 1
22        
23        return result
24                        