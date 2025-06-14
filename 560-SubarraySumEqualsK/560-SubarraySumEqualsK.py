# Last updated: 6/14/2025, 1:46:11 PM
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum = 0
        pref_counts = Counter({0:1})
        result = 0
        for num in nums:
            pref_sum += num
            diff = pref_sum - k
            if diff in pref_counts:
                result += pref_counts[diff]
            pref_counts[pref_sum] += 1

        return result