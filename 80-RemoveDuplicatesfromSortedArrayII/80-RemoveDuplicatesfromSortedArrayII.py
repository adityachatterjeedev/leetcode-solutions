# Last updated: 5/28/2025, 5:10:46 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = None
        count = 0
        write = 0

        for curr_num in nums:
            if curr_num != prev_num:
                prev_num = curr_num
                count = 1
            else:
                count += 1

            if count <= 2:
                nums[write] = curr_num
                write += 1

        return write