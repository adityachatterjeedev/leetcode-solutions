# Last updated: 3/22/2025, 10:47:45 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s > target :
                right -= 1
            elif s < target:
                left += 1
            else:
                return [left + 1, right + 1]