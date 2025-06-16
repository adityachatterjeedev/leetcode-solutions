# Last updated: 6/16/2025, 3:22:29 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pref = 0
        pref_pos = {0 : -1}
        result = 0
        for i, num in enumerate(nums):
            pref += (1 if num else -1)
            if (pref) in pref_pos:
                result = max(result, i - pref_pos[pref])
            else:
                pref_pos[pref] = i

        return result