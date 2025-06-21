# Last updated: 6/21/2025, 6:13:10 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left, agg, result = 0, 1, 0

        for right in range(len(nums)):
            agg *= nums[right]
            while agg >= k and left <= right:
                agg /= nums[left]
                left += 1
            result += right - left + 1


        return result