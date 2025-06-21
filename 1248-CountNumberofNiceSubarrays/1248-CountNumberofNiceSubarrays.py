# Last updated: 6/21/2025, 3:27:14 PM
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddidx=[-1]
        ans=0
        for i in range(len(nums)):
            if nums[i]%2:
                oddidx.append(i)
        oddidx.append(len(nums))
        for i in range(1,len(oddidx)-k):
            leftside=oddidx[i]-oddidx[i-1]
            rightside=oddidx[i+k]-oddidx[i+k-1]
            ans+=leftside*rightside
        return ans