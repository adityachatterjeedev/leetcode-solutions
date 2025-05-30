# Last updated: 5/29/2025, 9:12:24 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        k = 0
        while nums[k] != val:
            k += 1
            if k == len(nums):
                return k

        for i in range(k, len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        