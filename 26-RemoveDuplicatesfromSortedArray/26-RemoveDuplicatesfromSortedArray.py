# Last updated: 5/29/2025, 10:22:55 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_num_count = 0
        max_number_so_far = -500
        for i in range(len(nums)):
            if nums[i] > max_number_so_far:
                max_number_so_far = nums[i]
                nums[unique_num_count] = nums[i]
                unique_num_count += 1
        return unique_num_count