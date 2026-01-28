# Last updated: 1/28/2026, 2:27:54 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        low, high = 0, len(nums) - 1
4        
5        while low <= high:
6            mid = (low + high) // 2
7            if nums[mid] == target:
8                return mid
9            elif nums[mid] < target:
10                low = mid + 1
11            else:
12                high = mid - 1
13
14        return -1