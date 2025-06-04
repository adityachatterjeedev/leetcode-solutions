# Last updated: 6/4/2025, 4:13:32 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_elem = -100000
        k = 0 #write position
        elem_count = 1
        for num in nums:
            if num != prev_elem:
                prev_elem = num
                elem_count = 1
            else:
                elem_count += 1
            if elem_count <= 2:
                nums[k] = prev_elem
                k += 1
        return k