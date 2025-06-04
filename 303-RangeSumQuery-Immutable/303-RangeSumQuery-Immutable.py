# Last updated: 6/4/2025, 4:37:15 PM
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixes = [0 for _ in range(len(nums))]
        pref = 0
        for i, num in enumerate(nums):
            pref += num
            self.prefixes[i] = pref

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right] - (self.prefixes[left - 1] if left > 0 else 0) 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)