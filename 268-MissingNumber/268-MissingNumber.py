# Last updated: 3/24/2025, 10:53:34 AM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return ((n * (n + 1))//2) - sum(nums)