# Last updated: 5/28/2025, 5:04:00 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        smallest_num = -1e5
        count_of_smallest_num = 1 #invariant, always >= 1
        write = 0
        for curr_pos,curr_num in enumerate(nums):
            if curr_num > smallest_num:
                smallest_num = curr_num
                count_of_smallest_num = 1
            else:
                count_of_smallest_num += 1
            
            if count_of_smallest_num < 3:
                nums[write] = smallest_num
                write += 1
        
        return write
