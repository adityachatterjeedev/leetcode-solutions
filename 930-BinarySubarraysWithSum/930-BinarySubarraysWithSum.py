# Last updated: 6/21/2025, 3:34:05 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        num_sum, result = 0, 0
        pref_counts = {0 : 1}

        for num in nums:
            num_sum += num
            if num_sum >= goal:
                diff = num_sum - goal
                if diff in pref_counts:
                    result += pref_counts[diff]

            if num_sum in pref_counts:
                pref_counts[num_sum] += 1
            else:
                pref_counts[num_sum] = 1

        return result