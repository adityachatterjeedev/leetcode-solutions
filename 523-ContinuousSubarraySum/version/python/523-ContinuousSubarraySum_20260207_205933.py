# Last updated: 2/7/2026, 8:59:33 PM
1class Solution:
2    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
3        if len(nums) == 1:
4            return False
5        elif len(nums) == 2:
6            return (sum(nums) % k) == 0
7        
8        pref = 0
9        rems = {0 : -1}
10        for i, num in enumerate(nums):
11            pref += num
12            rem = pref % k
13            if rem not in rems:
14                rems[rem] = i
15            elif i - rems[rem] > 1:
16                return True
17                
18        return False
19        
20