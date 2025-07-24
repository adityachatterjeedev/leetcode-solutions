# Last updated: 7/24/2025, 1:32:56 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 100001
        left = 0
        current = 0
        for right, num in enumerate(nums):
            current += num
            while current >= target:
                result = min(result, right - left + 1)
                current -= nums[left]
                left += 1

        return 0 if result == 100001 else result