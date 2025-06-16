# Last updated: 6/16/2025, 3:23:04 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i == 0 or (nums[i - 1] != nums[i]):
                target = -num
                l, r = i + 1, len(nums) - 1
                while l < r:
                    total = nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        left = nums[l]
                        result += [[num, left, nums[r]]]
                        while nums[l] == left and l < r:
                            l += 1
        
        return result
                        