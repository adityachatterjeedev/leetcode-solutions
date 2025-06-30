# Last updated: 6/29/2025, 8:58:43 PM
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
            
            num -= 1
            if nums[num] > 0:
                nums[num] *= -1

        #find the missing positive
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return n + 1