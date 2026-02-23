# Last updated: 2/23/2026, 1:26:24 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stack = []
        dict_ = {}
        res = [0]*len(nums1)
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if stack:
                dict_[nums2[i]] = stack[-1]
            else:
                dict_[nums2[i]] = -1
            stack.append(nums2[i])

        for i in range(len(nums1)):
            res[i] = dict_[nums1[i]]

        return res 