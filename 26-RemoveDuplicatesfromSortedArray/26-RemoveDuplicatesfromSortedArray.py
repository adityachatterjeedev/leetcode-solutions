# Last updated: 5/29/2025, 10:25:34 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        max_number_so_far = -500
        for num in nums:
            if num > max_number_so_far:
                max_number_so_far = num
                nums[k] = num
                k += 1
        return k