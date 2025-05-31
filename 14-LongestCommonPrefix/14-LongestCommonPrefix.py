# Last updated: 5/31/2025, 7:01:28 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(pref):
                pref = pref[:-1]
                if pref == '':
                    return ''
        return pref