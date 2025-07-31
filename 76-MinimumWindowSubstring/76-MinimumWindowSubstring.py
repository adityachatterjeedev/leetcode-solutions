# Last updated: 7/31/2025, 5:08:58 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        t_counts = {}
        for c in t:
            t_counts[c] = 1 + t_counts.get(c, 0)
            
        flag, need = 0, len(t_counts)
        s_counts = {}
        res, res_len = [-1,-1], float("inf")
        left = 0

        for right, char in enumerate(s):
            if char in t_counts:
                s_counts[char] = 1 + s_counts.get(char, 0)

                if s_counts[char] == t_counts[char]:
                    flag += 1

                while flag == need:
                    if (right - left + 1) < res_len:
                        res = [left, right]
                        res_len = right - left + 1

                    if s[left] in t_counts:
                        s_counts[s[left]] -= 1
                        if s_counts[s[left]] < t_counts[s[left]]:
                            flag -= 1
                    left += 1

        return s[res[0] : res[1] + 1] if res_len != float('inf') else ''