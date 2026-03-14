# Last updated: 3/14/2026, 7:37:58 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = (left + right) // 2
7            if nums[mid] == target:
8                return True
9            elif nums[left] == nums[mid] == nums[right]:
10                left += 1
11                right -= 1
12            elif nums[mid] < target:
13                if nums[mid] < nums[left] <= target:
14                    right = mid - 1
15                else:
16                    left = mid + 1
17            else:
18                if target < nums[left] <= nums[mid]:
19                    left = mid + 1
20                else:
21                    right = mid - 1
22        return False