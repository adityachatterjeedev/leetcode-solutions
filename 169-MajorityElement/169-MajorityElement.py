# Last updated: 5/29/2025, 10:26:15 PM
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
