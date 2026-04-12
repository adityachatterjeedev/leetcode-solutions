# Last updated: 4/12/2026, 12:27:13 AM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4        candidates.sort()
5
6        def dfs(i, curr, remaining):
7            if remaining == 0:
8                res.append(curr.copy())
9                return
10
11            
12            for j in range(i, len(candidates)):
13                if j > i and candidates[j] == candidates[j - 1]:
14                    continue
15                
16                if candidates[j] > remaining:
17                    break
18                
19                curr.append(candidates[j])
20                dfs(j + 1, curr, remaining - candidates[j])
21                curr.pop()
22
23        dfs(0, [], target)
24        return res     