# Last updated: 4/4/2025, 4:35:41 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            num1 = nums[i]
            if num1 > 0:
                break
            if i > 0 and num1 == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = num1 + nums[left] + nums[right]
                if total == 0:
                    result.append([num1, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
                


