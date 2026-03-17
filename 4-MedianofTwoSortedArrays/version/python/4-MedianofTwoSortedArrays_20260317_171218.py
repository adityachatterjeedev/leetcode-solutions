# Last updated: 3/17/2026, 5:12:18 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        A,B = nums1, nums2
4
5        if len(nums2) < len(nums1):
6            A, B = B, A
7
8        m, n = len(A), len(B)
9
10        total = m + n
11
12        half = total // 2
13
14        l, r = 0, m - 1
15
16        while True:
17            mid = (l + r) // 2
18
19            B_ptr = half - mid - 2
20
21            Aleft = A[mid] if mid >= 0 else float('-inf')
22            Aright = A[mid + 1] if ((mid + 1) < m) else float('inf')
23            Bleft = B[B_ptr] if B_ptr >= 0 else float('-inf')
24            Bright = B[B_ptr + 1] if ((B_ptr + 1) < n) else float('inf')
25
26            if Aleft > Bright:
27                r = mid - 1
28            elif Bleft > Aright:
29                l = mid + 1
30            else:
31                if total % 2:
32                    return min(Aright, Bright)
33                else:
34                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2