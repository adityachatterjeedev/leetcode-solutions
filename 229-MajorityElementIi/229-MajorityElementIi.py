# Last updated: 6/16/2025, 3:22:37 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = None
        c1 = c2 = 0
        t = len(nums)//3
        for i in nums:
            if i == n1:
                c1+=1
            elif i == n2:
                c2+=1
            elif c1 == 0:
                n1 = i
                c1 = 1
            elif c2 == 0:
                n2 = i
                c2 = 1
            
            else:
                c1-=1
                c2-=1
        c1 = c2 = 0
        r = []
        for i in nums:
            if i == n1:
                c1+=1
            elif i == n2:
                c2+=1

        if c1> t:
            r.append(n1)
        if c2> t:
            r.append(n2)
        return r

            