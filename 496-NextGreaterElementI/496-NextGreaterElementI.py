# Last updated: 7/7/2026, 6:36:20 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)

        ng = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                ng[stack.pop()] = num
            stack.append(num)

        for i, n in enumerate(nums1):
            if n in ng:
                ans[i] = ng[n]


        return ans