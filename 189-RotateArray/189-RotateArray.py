# Last updated: 5/21/2025, 6:33:02 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_len = len(nums)
        k = k % arr_len

        def reverse(i, j):
            l, r = i, j
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        # reverse the whole array
        reverse(0, arr_len - 1)

        #reverse first k
        reverse(0, k - 1)

        reverse(k, arr_len - 1)