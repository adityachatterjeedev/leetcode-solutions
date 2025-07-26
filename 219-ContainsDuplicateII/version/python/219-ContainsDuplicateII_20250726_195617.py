# Last updated: 7/26/2025, 7:56:17 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numset = set()
        for i in range(len(nums)):
            if nums[i] in numset:
                return True
            numset.add(nums[i])
            if len(numset) > k:
                numset.remove(nums[i - k])
        return False