# Last updated: 7/19/2025, 8:45:26 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for a in range(n - 3):
            x = nums[a]

            if a and nums[a] == nums[a - 1]:
                continue
            
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break

            if x + nums[-1] + nums[-2] + nums[-3] < target:
                continue

            for b in range(a + 1, n - 2):
                y = nums[b]

                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                
                if x + y + nums[b + 1] + nums[b + 2] > target:
                    break
                
                if x + y + nums[-1] + nums[-2] < target:
                    continue

                c = b + 1
                d = n - 1
                while c < d:
                    s = x + y + nums[c] + nums[d]

                    if s < target:
                        c += 1
                    elif s > target:
                        d -= 1
                    else:
                        ans.append([x, y, nums[c], nums[d]])

                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
        
        return ans
            