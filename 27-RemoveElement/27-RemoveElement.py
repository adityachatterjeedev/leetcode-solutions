# Last updated: 5/20/2025, 2:30:27 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        i, k = 0, len(nums) - 1
        while i <= k:
            if nums[i] == val:
                swap(i,k)
                k -= 1
            else:
                i += 1
        return k+1

        