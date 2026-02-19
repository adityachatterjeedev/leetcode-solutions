# Last updated: 2/19/2026, 3:15:24 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones_count = 0
        max_ones = 0
        left = 0
        window_size = 0
        res = 0
        for right in range(len(nums)):
            digit = nums[right]
            window_size += 1
            if digit == 1:
                ones_count += 1
            if ones_count > max_ones:
                max_ones = ones_count
            while (window_size - max_ones) > k:
                if nums[left] == 1:
                    ones_count -= 1
                left += 1
                window_size -= 1

            if window_size > res:
                res = window_size
        
        return res
            
            