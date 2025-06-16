# Last updated: 6/16/2025, 3:22:25 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxScore = 0
        lst = []
        start = 0
        end = 0
        length = len(nums)
        while end <= (length - 1):
            num = nums[end]
            if num in lst:
                start = nums.index(num, start, end) + 1
            end += 1
            lst = nums[start:end]
            maxScore = max(maxScore, sum(lst))
        return maxScore