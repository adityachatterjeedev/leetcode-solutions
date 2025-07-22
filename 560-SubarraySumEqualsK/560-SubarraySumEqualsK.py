# Last updated: 7/22/2025, 7:24:05 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in prefs:
                count += prefs[curr_sum - k]
            prefs[curr_sum] = 1 + prefs.get(curr_sum, 0)

        return count