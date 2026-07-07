# Last updated: 7/7/2026, 6:36:19 PM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []

        res = [-1] * len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                res[stack.pop()[1]] = num
            stack.append((num, i))

        for num in nums:
            while stack and stack[-1][0] < num:
                res[stack.pop()[1]] = num

        return res