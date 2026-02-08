# Last updated: 2/8/2026, 3:49:14 AM
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []

        quot = num // 3

        return [quot -1, quot, quot + 1]