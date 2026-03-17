# Last updated: 3/17/2026, 5:15:35 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = (len(nums1)+len(nums2))
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1
        half= total//2
        l = 0
        r = len(nums1)

        while l<=r:
            mid= l+(r-l)//2

            mid2 = half-mid

            l1 = nums1[mid-1] if mid>0 else -inf
            l2 = nums2[mid2-1] if mid2>0 else -inf
            r1 = nums1[mid] if mid<len(nums1) else inf
            r2 = nums2[mid2] if mid2<len(nums2) else inf

            if l1<=r2 and l2<=r1:
                if total%2:
                    return min(r1,r2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                r=mid-1
            else:
                l=mid+1

