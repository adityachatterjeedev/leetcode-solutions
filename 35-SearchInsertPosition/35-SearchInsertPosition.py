# Last updated: 3/24/2025, 10:57:08 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        while (end - start) > 0:
            if nums[mid] < target:
                start = mid + 1
            elif nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            else:
                end = mid
            
            mid = (start + end) // 2

        if nums[mid] < target:
            return mid + 1
        else:
            return mid