# Last updated: 5/29/2025, 10:40:36 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = [1] * len(nums)

        #prefix prods
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        #suffix prods
        suff = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suff
            suff *= nums[i]
        return result