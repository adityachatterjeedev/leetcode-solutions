# Last updated: 6/16/2025, 3:22:40 PM
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n = n // 2
        return count