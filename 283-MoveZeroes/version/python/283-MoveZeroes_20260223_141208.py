# Last updated: 2/23/2026, 2:12:08 PM
1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        writePos = 0
7        for num in nums:
8            if num == 0:
9                continue
10            nums[writePos] = num
11            writePos += 1
12
13        for i in range(writePos, len(nums)):
14            nums[i] = 0