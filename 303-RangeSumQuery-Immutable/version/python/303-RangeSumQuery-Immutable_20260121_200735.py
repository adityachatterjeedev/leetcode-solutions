# Last updated: 1/21/2026, 8:07:35 PM
1class NumArray:
2
3    def __init__(self, nums: List[int]):
4        self.nums = nums
5        self.prefs = [0] * (len(nums) + 1)
6        cum_sum = 0
7        for i, num in enumerate(nums):
8            cum_sum += num
9            self.prefs[i + 1] = cum_sum
10
11    def sumRange(self, left: int, right: int) -> int:
12        return self.prefs[right + 1] - self.prefs[left]
13
14
15# Your NumArray object will be instantiated and called as such:
16# obj = NumArray(nums)
17# param_1 = obj.sumRange(left,right)