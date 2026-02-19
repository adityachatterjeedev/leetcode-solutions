# Last updated: 2/19/2026, 3:24:54 AM
1class Solution:
2    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
3        counts = {'T' : 0, 'F' : 0}
4        res = 0
5        maxf = 0
6        window_size = 0
7        left = 0
8        for right, answer in enumerate(answerKey):
9            counts[answer] += 1
10            window_size += 1
11            if counts[answer] > maxf:
12                maxf = counts[answer]
13            while (window_size - maxf) > k:
14                counts[answerKey[left]] -= 1
15                left += 1
16                window_size -= 1
17            if window_size > res:
18                res = window_size
19
20        return res