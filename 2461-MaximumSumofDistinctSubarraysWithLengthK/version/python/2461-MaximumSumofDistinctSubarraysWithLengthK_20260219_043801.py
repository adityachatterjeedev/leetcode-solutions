# Last updated: 2/19/2026, 4:38:01 AM
1class Solution:
2    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
3        res = 0
4        current_sum = 0
5        elements = set()
6        left = 0
7        window_size = 0
8
9        for right in range(len(nums)):
10            # If we hit a duplicate, shrink until the duplicate is gone
11            while nums[right] in elements:
12                elements.remove(nums[left])
13                current_sum -= nums[left]
14                left += 1
15                window_size -= 1
16
17            elements.add(nums[right])
18            current_sum += nums[right]
19            window_size += 1
20
21            # If the window is too big, shrink it from the left
22            if window_size > k:
23                elements.remove(nums[left])
24                current_sum -= nums[left]
25                left += 1
26                window_size -= 1
27            
28            if window_size == k and current_sum > res:
29                res = current_sum
30                
31        return res