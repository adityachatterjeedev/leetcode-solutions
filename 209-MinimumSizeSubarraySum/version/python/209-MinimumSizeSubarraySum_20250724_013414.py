# Last updated: 7/24/2025, 1:34:14 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans=1e8
        cur=0
        for right in range(len(nums)):
            cur+=nums[right]
            while cur>=target:
                ans=min(right-left+1,ans)
                cur-=nums[left]
                left+=1
        return ans if ans!=1e8 else 0