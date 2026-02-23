# Last updated: 2/23/2026, 2:24:02 PM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        return list(set(nums1).intersection(set(nums2)))