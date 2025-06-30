# Last updated: 6/29/2025, 8:58:15 PM
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        indices = [i for i, num in enumerate(nums) if num == max_num]
        result = 0
        n = len(nums)

        for i in range(len(indices) - k + 1):
            left = indices[i]
            right = indices[i + k - 1]
            result += (left - (indices[i - 1] if i > 0 else -1)) * (n - right)

        return result