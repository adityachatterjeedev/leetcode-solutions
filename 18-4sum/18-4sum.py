# Last updated: 7/22/2025, 9:56:03 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        a = 0

        while a < n - 3:
            x = nums[a]

            # Early termination: smallest possible sum > target
            if x + nums[a + 1] + nums[a + 2] + nums[a + 3] > target:
                break

            # Skip if largest possible sum is still too small
            if x + nums[-1] + nums[-2] + nums[-3] < target:
                a += 1
                while a < n - 3 and nums[a] == nums[a - 1]:
                    a += 1
                continue

            b = a + 1
            while b < n - 2:
                y = nums[b]

                # Early termination on second index
                if x + y + nums[b + 1] + nums[b + 2] > target:
                    break
                if x + y + nums[-1] + nums[-2] < target:
                    b += 1
                    while b < n - 2 and nums[b] == nums[b - 1]:
                        b += 1
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
                        res.append([x, y, nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1

                b += 1
                while b < n - 2 and nums[b] == nums[b - 1]:
                    b += 1

            a += 1
            while a < n - 3 and nums[a] == nums[a - 1]:
                a += 1

        return res