# Last updated: 7/19/2025, 8:34:29 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        e1 = 0
        length = len(nums)
        result = []
        while e1 < length - 3:
            e2 = e1 + 1
            while e2 < length - 2:
                goal = target - (nums[e1] + nums[e2])
                left, right = e2 + 1, length - 1
                while left < right:
                    total = nums[left] + nums[right]
                    if total == goal:
                        result.append([nums[e1], nums[e2], nums[left], nums[right]])
                        n = left + 1
                        while n < right and nums[n] == nums[n - 1]:
                            n += 1
                        left = n
                    elif total < goal:
                        left += 1
                    else:
                        right -= 1

                nxt = e2 + 1
                while nxt < length - 2 and nums[nxt] == nums[nxt - 1]:
                    nxt += 1
                e2 = nxt
            
            nextindex = e1 + 1
            while nextindex < length - 3 and nums[nextindex] == nums[nextindex - 1]:
                nextindex += 1
            e1 = nextindex

        return result