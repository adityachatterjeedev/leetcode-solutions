# Last updated: 3/22/2025, 11:01:18 PM
def compareTwoStrings(string1: str, string2: str) -> str:
    if not string1 or not string2:
        return ''
    length = min(len(string1), len(string2))
    for i in range (length):
        if string1[i] != string2[i]:
            if i == 0:
                return ''
            else:
                return string1[:i]
        elif i == length - 1:
            return string1[:i+1]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            prefix = compareTwoStrings(prefix, strs[i])
            if prefix == '': return prefix
        return prefix