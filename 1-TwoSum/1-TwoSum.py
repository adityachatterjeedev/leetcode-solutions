# Last updated: 6/16/2025, 3:23:07 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        items = dict()
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if num in items:
                return [i, items[num]]
            else:
                items[diff] = i

        