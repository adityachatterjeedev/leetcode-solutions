# Last updated: 6/14/2025, 6:52:06 AM
class Solution:
    def majorityElement(self, a: List[int]) -> List[int]:
        n1 = n2 = None
        c1 = c2 = 0
        t = len(a)//3
        for i in a:
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
        for i in a:
            if i == n1:
                c1+=1
            elif i == n2:
                c2+=1
        print(t)
        print(n1,c1)
        print(n2,c2)
        if c1> t:
            r.append(n1)
        if c2> t:
            r.append(n2)
        return r