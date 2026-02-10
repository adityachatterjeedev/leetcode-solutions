# Last updated: 2/10/2026, 3:46:55 AM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        if k == 0:
4            return False
5        if k > len(nums):
6            k = len(nums)
7        contents = set(nums[:k])
8        if len(contents) < k:
9            return True
10        left, right = 0, k - 1
11        while right < len(nums) - 1:
12            if nums[right + 1] in contents:
13                return True
14            else:
15                contents.remove(nums[left])
16                left += 1
17                right += 1
18                contents.add(nums[right])
19
20        return False