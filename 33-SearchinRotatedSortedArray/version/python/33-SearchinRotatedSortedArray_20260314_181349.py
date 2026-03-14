# Last updated: 3/14/2026, 6:13:49 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = (left + right) // 2
7
8            if nums[mid] == target:
9                return mid
10            elif nums[mid] > target:
11                if nums[left] <= target:
12                    right = mid - 1
13                else:
14                    if nums[left] <= nums[mid]:
15                        left = mid + 1
16                    else:
17                        right = mid - 1
18            else: # nums[mid] < target
19                if nums[mid] < nums[left]:
20                    if nums[left] <= target:
21                        right = mid - 1
22                    else:
23                        left = mid + 1
24                else:
25                    left = mid + 1
26        return -1