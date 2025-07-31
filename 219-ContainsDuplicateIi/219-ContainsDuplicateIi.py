# Last updated: 7/31/2025, 5:08:44 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, j in enumerate(nums):
            if j in seen and i - seen[j] <=k:
                return True
            else:
                seen[j] = i
        return False