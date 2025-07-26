# Last updated: 7/26/2025, 1:54:25 AM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(len(nums)):
            num = abs(nums[i])
            if num > n:
                continue

            if nums[num - 1] > 0:
                nums[num - 1] *= -1

        #find the missing positive
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1