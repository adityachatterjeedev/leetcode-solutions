# Last updated: 6/14/2025, 4:37:28 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore's Voting Algorithm
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num != candidate:
                count -= 1
            else:
                count += 1
        
        return candidate

