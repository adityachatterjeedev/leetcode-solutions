# Last updated: 4/9/2026, 8:51:43 PM
1class Solution:
2    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
3        res = []
4
5        nums.sort()
6
7        def dfs(i, curr, total):
8            if total == target:
9                res.append(curr.copy())
10                return
11            
12            for j in range(i, len(nums)):
13                if total + nums[j] > target:
14                    break
15                curr.append(nums[j])
16                dfs(j, curr, total + nums[j])
17                curr.pop()
18
19        dfs(0, [], 0)
20        return res     