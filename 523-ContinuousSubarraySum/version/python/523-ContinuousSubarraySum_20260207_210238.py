# Last updated: 2/7/2026, 9:02:38 PM
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ## (prefixSum[j] - prefixSum[i]) % k == 0
        ##  prefixSum[j] % k == prefixSum[i] % k
        lookup = dict()

        predix_sum=0
        for i, num in enumerate(nums):
            predix_sum+=num
            mod = predix_sum%k
            if mod == 0 and i >=1 :
                return True
            if mod not in lookup:
                lookup[mod]=i
            elif i - lookup[mod] >=2:
                return True
        return False

        