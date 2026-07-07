# Last updated: 7/7/2026, 6:36:24 PM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        l, r = max(nums), sum(nums)

        res = r

        while l <= r:
            mid = (l + r) // 2

            arr_count = 1

            curr_sum = 0

            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    arr_count += 1
                    curr_sum = num
            
            if arr_count <= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res