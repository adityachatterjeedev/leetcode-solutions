# Last updated: 6/2/2025, 1:49:31 AM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)       
        if n == 2:
            return [1,2]
        
        left = 0
        right = n-1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left+1, right+1]
            elif target < curr:
                right -= 1
            else:
                left += 1
        

        