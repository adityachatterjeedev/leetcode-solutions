# Last updated: 7/25/2025, 8:31:30 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = 1e8
        left = 0
        current = 0
        for right in range(len(nums)):
            current += nums[right]
            while current >= target:
                if (right - left + 1) < result:
                    result = right - left + 1
                current -= nums[left]
                left += 1

        return 0 if result == 1e8 else result