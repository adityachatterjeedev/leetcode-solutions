# Last updated: 7/26/2025, 8:08:54 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefs = [0] * n
        suffs = [0] * n

        prefs[0] = height[0]
        maxPref = height[0]
        for i in range(1, n):
            if height[i] > maxPref:
                maxPref = height[i]
            prefs[i] = maxPref

        suffs[n - 1] = height[n - 1]
        maxSuff = height[n - 1]
        for i in range(n - 2, -1, -1):
            if height[i] > maxSuff:
                maxSuff = height[i]
            suffs[i] = maxSuff

        result = 0
        for i in range(n):
            result += min(prefs[i], suffs[i]) - height[i]

        return result