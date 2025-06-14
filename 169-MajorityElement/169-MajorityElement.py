# Last updated: 6/14/2025, 4:38:06 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        key = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == key:
                count += 1
            else:
                count -= 1

            if count == 0:
                key = nums[i]
                count = 1

        return key