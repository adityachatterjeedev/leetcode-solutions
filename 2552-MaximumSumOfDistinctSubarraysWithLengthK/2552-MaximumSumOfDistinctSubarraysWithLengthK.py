# Last updated: 2/22/2026, 7:57:17 PM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        current_sum = 0
        elements = set()
        left = 0
        window_size = 0

        for right in range(len(nums)):
            # If we hit a duplicate, shrink until the duplicate is gone
            while nums[right] in elements:
                elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
                window_size -= 1

            elements.add(nums[right])
            current_sum += nums[right]
            window_size += 1

            # If the window is too big, shrink it from the left
            if window_size > k:
                elements.remove(nums[left])
                current_sum -= nums[left]
                left += 1
                window_size -= 1
            
            if window_size == k and current_sum > res:
                res = current_sum
                
        return res