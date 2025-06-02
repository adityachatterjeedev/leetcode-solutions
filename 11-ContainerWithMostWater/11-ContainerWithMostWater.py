# Last updated: 6/2/2025, 3:52:56 AM
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                max_area = max(max_area, heights[l] * (r - l))
                l += 1
            else:
                max_area = max(max_area, heights[r] * (r - l))
                r -= 1
        return max_area