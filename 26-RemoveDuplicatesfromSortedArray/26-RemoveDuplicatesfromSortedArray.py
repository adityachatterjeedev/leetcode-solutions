# Last updated: 3/22/2025, 11:06:24 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        contentsSet = set()
        i = 0
        length = len(nums)
        while i <= length - 1:
            if nums[i] in contentsSet:
                nums.pop(i)
                length -= 1
            else:
                contentsSet.add(nums[i])
                i += 1
        return len(nums)