# Last updated: 6/14/2025, 6:48:32 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length in [0,1]:
            return nums
        elif length == 2:
            if nums[0] == nums[1]:
                return [nums[0]]
            else:
                return nums
        
        #Hashmap
        counts = {}
        result = []
        boundary = (length // 3) + 1
        for num in nums:
            if num in counts:
                counts[num] += 1
                if counts[num] == boundary:
                    result.append(num)
                    if len(result) == 2:
                        return result
            else:
                counts[num] = 1

        return result

            