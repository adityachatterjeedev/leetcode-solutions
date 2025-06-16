# Last updated: 6/16/2025, 3:22:39 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)