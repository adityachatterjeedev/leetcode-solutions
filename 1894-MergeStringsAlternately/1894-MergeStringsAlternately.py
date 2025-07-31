# Last updated: 7/31/2025, 5:08:30 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        c1, c2 = 0,0
        flag = True
        result = ''
        while c1 + c2 < n1 + n2:
            if c1 == n1:
                result += word2[c2]
                c2 += 1
            elif c2 == n2:
                result += word1[c1]
                c1 += 1
            elif flag:
                result += word1[c1]
                c1 += 1
                flag = not flag
            else:
                result += word2[c2]
                c2 += 1
                flag = not flag
        return result