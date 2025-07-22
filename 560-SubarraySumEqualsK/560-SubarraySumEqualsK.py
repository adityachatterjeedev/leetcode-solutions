# Last updated: 7/22/2025, 7:25:12 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefs = {0: 1}
        curr_sum = 0
        count = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in prefs:
                count += prefs[diff]
            prefs[curr_sum] = 1 + prefs.get(curr_sum, 0)

        return count