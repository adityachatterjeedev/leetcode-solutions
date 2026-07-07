# Last updated: 7/7/2026, 6:36:35 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writePos = 0
        for num in nums:
            if num == 0:
                continue
            nums[writePos] = num
            writePos += 1

        for i in range(writePos, len(nums)):
            nums[i] = 0