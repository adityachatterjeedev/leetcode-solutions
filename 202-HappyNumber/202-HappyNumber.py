# Last updated: 3/24/2025, 10:51:44 AM
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        temp = n
        while temp > 1:
            count = 0
            num = temp
            while num > 0:
                count += ((num % 10) ** 2)
                num = num // 10
            if count in s:
                return False
            else:
                s.add(count)
                temp = count
        
        return True
        