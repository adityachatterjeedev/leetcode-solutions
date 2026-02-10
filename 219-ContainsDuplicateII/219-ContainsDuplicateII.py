# Last updated: 2/10/2026, 3:47:13 AM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        numset = set()
4        for i in range(len(nums)):
5            if nums[i] in numset:
6                return True
7            numset.add(nums[i])
8            if len(numset) > k:
9                numset.remove(nums[i - k])
10        return False