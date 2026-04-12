# Last updated: 4/12/2026, 12:28:41 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        li=[]
        result=[]
        candidates.sort()
        def backtrack(index,target):
            if(target==0):
                result.append(li[:])
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if(candidates[i]>target):
                    break    
                li.append(candidates[i])
                backtrack(i+1,target-candidates[i])   
                li.pop()
            
        backtrack(0,target)
        
        return result         