# Last updated: 7/26/2025, 2:12:52 AM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #three loops
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            num = -nums[i] if nums[i] < 0 else nums[i]

            if num > n:
                continue
            
            if nums[num - 1] > 0:
                nums[num - 1] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1