# Last updated: 3/13/2026, 4:01:33 PM
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        l, r = 1, n
11
12        while l <= r:
13            mid = (l + r) // 2
14            res = guess(mid)
15            if res == 0:
16                return mid
17            elif res == 1:
18                l = mid + 1
19            else:
20                r = mid - 1
21
22        return l
23        