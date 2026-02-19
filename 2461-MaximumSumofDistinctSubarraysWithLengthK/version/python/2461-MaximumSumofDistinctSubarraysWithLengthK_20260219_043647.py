# Last updated: 2/19/2026, 4:36:47 AM
1class Solution:
2    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
3        res = 0
4        current_sum = 0
5        elements = set()
6        left = 0
7
8        for right in range(len(nums)):
9            # If we hit a duplicate, shrink until the duplicate is gone
10            while nums[right] in elements:
11                elements.remove(nums[left])
12                current_sum -= nums[left]
13                left += 1
14
15            elements.add(nums[right])
16            current_sum += nums[right]
17
18            # If the window is too big, shrink it from the left
19            if right - left + 1 > k:
20                elements.remove(nums[left])
21                current_sum -= nums[left]
22                left += 1
23            
24            if right - left + 1 == k:
25                res = max(res, current_sum)
26                
27        return res