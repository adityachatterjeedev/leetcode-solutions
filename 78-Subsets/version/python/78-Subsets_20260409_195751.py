# Last updated: 4/9/2026, 7:57:51 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        le = len(nums)
5
6        def recurse(ind, agg):
7            if ind == le:
8                res.append(agg)
9            else:
10                recurse(ind + 1, agg + [nums[ind]])
11                recurse(ind + 1, agg)
12
13        recurse(0, [])
14        return res      