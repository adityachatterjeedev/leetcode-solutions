# Last updated: 5/31/2025, 7:02:02 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        ans=strs[0]

        for i in strs:
            while not i.startswith(ans): 
                ans= ans[:-1]
                if not ans:
                    return ""

        return ans 





        