# Last updated: 7/26/2025, 8:05:22 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefs = [0] * n
        suffs = [0] * n

        maxPref = 0
        for i in range(n):
            if height[i] > maxPref:
                maxPref = height[i]
            prefs[i] = maxPref

        maxSuff = 0
        for i in range(n - 1, -1, -1):
            if height[i] > maxSuff:
                maxSuff = height[i]
            suffs[i] = maxSuff

        result = 0
        for i in range(n):
            result += min(prefs[i], suffs[i]) - height[i]

        return result