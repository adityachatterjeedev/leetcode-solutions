# Last updated: 6/4/2025, 5:53:12 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's Voting Algorithm

        el, count = None, 0
        for num in nums:
            if count == 0:
                el = num
                count = 1
            elif num == el:
                count += 1
            else:
                count -= 1

        return el
