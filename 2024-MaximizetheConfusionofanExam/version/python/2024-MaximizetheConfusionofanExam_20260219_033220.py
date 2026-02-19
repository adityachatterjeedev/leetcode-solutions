# Last updated: 2/19/2026, 3:32:20 AM
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        le=len(answerKey)
        ans=0
        ct=0
        cf=0
        for r in range(le):
            if(answerKey[r]=="T"):
                ct+=1
            else:
                cf+=1
            while(min(ct,cf)>k):
                if(answerKey[l]=="T"):
                    ct-=1
                else:
                    cf-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans