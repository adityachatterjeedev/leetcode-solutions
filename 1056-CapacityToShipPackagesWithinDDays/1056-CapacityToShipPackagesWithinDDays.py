# Last updated: 7/7/2026, 6:36:03 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        if days == 1:
            return sum(weights)

        l, r = max(weights), sum(weights)

        res = r
        while l <= r:
            mid = (l + r) // 2

            day_count = 1
            weight_sum = 0
            for weight in weights: 
                weight_sum += weight
                if weight_sum > mid:
                    day_count += 1
                    weight_sum = weight

                
            if day_count > days:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
            
        return res