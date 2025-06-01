# Last updated: 6/1/2025, 3:20:46 AM
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)

        bins = [[] for _ in range(len(nums) + 1)]
        for item,count in counts.items():
            bins[count].append(item)

        result = []
        for i in range(len(nums), -1, -1):
            result += bins[i]
            if len(result) >= k:
                break
        
        return result[:k]