# Last updated: 2/8/2026, 3:49:23 AM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        pref = 0
        rems = {0 : -1}
        for i, num in enumerate(nums):
            pref += num
            rem = pref % k
            if rem not in rems:
                rems[rem] = i
            elif i - rems[rem] > 1:
                return True

        return False