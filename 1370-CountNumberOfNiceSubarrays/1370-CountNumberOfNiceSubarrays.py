# Last updated: 6/29/2025, 8:58:14 PM
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        counts = {0: 1}

        result = 0

        for num in nums:
            odd_count += num % 2
            if odd_count >= k:
                diff = odd_count - k
                if diff in counts:
                    result += counts[diff]
            
            if odd_count in counts:
                counts[odd_count] += 1
            else:
                counts[odd_count] = 1

        return result