# Last updated: 3/24/2025, 10:49:48 AM
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
